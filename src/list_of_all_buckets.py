import boto3

# Create a session with AWS credentials
session = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key'
)

# Create an S3 resource using the session
s3 = session.resource('s3')

# List all buckets
for bucket in s3.buckets.all():
    print(bucket.name)
