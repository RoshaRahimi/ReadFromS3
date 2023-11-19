import boto3

BUCKET_NAME = "peckwater-data"

session = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key'
)
s3 = session.client("s3")

# Upload file to bucket
with open('./IMG.jpg' , 'rb') as f:
    s3.upload_fileobj(f, BUCKET_NAME, 'IMG.jpg')