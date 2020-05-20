# Web projects practising AWS Cloud Computing Services like S3 Bucket, DynamoDB, Lambda etc.

There are different django and flask web projects under this repository. 

In first project I used AWS S3 Bucket to upload image.

In second project I improved first project and integrated with dynamoDB. Metadata information of the uploaded object is written to Dynamo DB.

In third project, in addition to S3 and Dynamo DB software that I have developed in the previous projects, I created a simple interface. In this interface an API Gateway is triggered so that CRUD operations achieved using Lambda. 


## aws-s3bucket-django-app

### Django app that uploads image given by the user to Amazon S3 bucket

Before running the project you should create an AWS account then create an AWS S3 bucket in the console.

After defining AWS Cli credentials, you should fill credentials in setting.py about s3 bucket that you have created. 

The required araeas are AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME in the settings.py.
 

You should run following commands to run the project.

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver



## aws-dynamodb-s3bucket-flask-app

### This is a Flask web application integrated with Amazon S3 Bucket and DynamoDB.

To run the application;

- Install requirement.txt
- Define crediantials in config.py 
- Type "flask run" command
