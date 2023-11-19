import boto3

BUCKET_NAME = 'peckwater-data'
session = boto3.Session(
    aws_access_key_id='AKIAVC3ZYDBG5UCTBKGH',
    aws_secret_access_key='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'
)

s3 = session.client('s3')
s3.download_file(BUCKET_NAME, 'IMG.jpg', 'IMG_Download.jpg')
