import boto3

BUCKET_NAME = 'peckwater-data'
session = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key',
    region_name='eu-west-1'
)

s3 = session.client('s3')
s3.copy_object(
    ACL='public-read',
    Bucket='peckwater-data',
    CopySource=f'/{BUCKET_NAME}/IMG.jpg',
    Key='copiedIMG.jpg'

)