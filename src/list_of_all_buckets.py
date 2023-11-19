import boto3

# Create a session with AWS credentials
session = boto3.Session(
    aws_access_key_id='AKIAVC3ZYDBG5UCTBKGH',
    aws_secret_access_key='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'
)

# Create an S3 resource using the session
s3 = session.resource('s3')

# List all buckets
for bucket in s3.buckets.all():
    print(bucket.name)
