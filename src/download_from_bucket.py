import boto3

BUCKET_NAME = 'peckwater-data'
session = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key'
)

s3 = session.client('s3')
s3.download_file(BUCKET_NAME, 'IMG.jpg', 'IMG_Download.jpg')
