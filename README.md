# Django and Flask web projects practising AWS Cloud Computing Services like S3 Bucket, DynamoDB, Lambda etc.

## aws-s3bucket-django-app

### Django app that uploads image given by the user to Amazon S3 bucket

Before running the project you should create an AWS account then create an AWS S3 bucket in the console.

After defining AWS Cli credentials, you should fill credentials in setting.py about s3 bucket that you have created. 

The required araeas are AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME in the settings.py.
 

You should run following commands to run the project.

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

