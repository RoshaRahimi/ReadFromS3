import boto3

session = boto3.Session(
    aws_access_key_id='AKIAVC3ZYDBG5UCTBKGH',
    aws_secret_access_key='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',
    region_name='eu-west-1'
)

s3 = session.client('s3')
bucket_location = s3.create_bucket(
    Bucket='new-buck-peck-900',
    CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'}
)
print(bucket_location)