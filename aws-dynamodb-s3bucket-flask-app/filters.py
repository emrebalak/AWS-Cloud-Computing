import os
import mimetypes
import arrow

from botocore.exceptions import NoCredentialsError, ClientError
import datetime
import boto3
from flask import request

def datetimeformat(date_str):
    dt = arrow.get(date_str)
    return dt.humanize()


def file_type(key):
    file_info = os.path.splitext(key)
    file_extension = file_info[1]
    try:
        return mimetypes.types_map[file_extension]
    except Exception as e:
        return 'Unknown'


def put_dbitem(table_name, file):
    createTable(table_name)

    file.seek(0, os.SEEK_END) # go to the end of file 
    file_size = (str(file.tell()/1000)) # byte to kb coverted position of seek() 

    filename = file.filename
    current_time = (datetime.date.today().strftime("%Y-%m-%d"))
    file_extension = file_type(file.filename)

    db = boto3.resource('dynamodb', region_name="eu-central-1")
    table = db.Table(table_name)
    table.put_item(Item={'name':filename,'date':current_time,
                         'file_size(kb)':file_size,'file_extension': file_extension})
    return


def list_tables():
    db = boto3.resource('dynamodb', region_name="eu-central-1")
    tables = list(db.tables.all())
    return tables 


def createTable(table_name):
    error = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb', region_name="eu-central-1")
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'  #Partition key
                },
                {
                    'AttributeName': 'date',
                    'KeyType': 'RANGE'  #Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'date',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    except ClientError:
        return dynamodb #Existing table name given

    return dynamodb
