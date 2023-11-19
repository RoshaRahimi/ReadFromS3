import boto3

session = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key',
    region_name='eu-west-1'
)

s3 = session.client('s3')
bucket_location = s3.create_bucket(
    Bucket='new-buck-peck-900',
    CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'}
)
print(bucket_location)