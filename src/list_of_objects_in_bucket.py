# import boto3
import boto3

BUCKET_NAME = 'peckwater-data'

# Create a session with AWS credentials
session = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key'
)

# Create an S3 client using the session
s3 = session.client('s3')

# get the list of metadata of the objects inside the bucket
response = s3.list_objects_v2(Bucket = BUCKET_NAME)
for obj in response["Contents"]:
    print(obj)
