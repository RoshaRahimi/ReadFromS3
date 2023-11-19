import boto3

BUCKET_NAME = 'peckwater-data'
session = boto3.Session(
    aws_access_key_id='AKIAVC3ZYDBG5UCTBKGH',
    aws_secret_access_key='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',
    region_name='eu-west-1'
)

s3 = session.client('s3')
response = s3.get_object(Bucket=BUCKET_NAME, Key='IMG.jpg')
print(response)