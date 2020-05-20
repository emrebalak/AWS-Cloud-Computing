from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
import boto3


from .models import Document, PrivateDocument


class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context


class PrivateDocumentCreateView(CreateView):
    model = PrivateDocument
    fields = ['upload', ]
    success_url = reverse_lazy('private')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = PrivateDocument.objects.all()
        context['documents'] = documents
        return context

def createTable(table_name):
    error = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
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
    except ClientError:
        #if table already exists then return
        return dynamodb
    return dynamodb