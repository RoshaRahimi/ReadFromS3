import boto3

BUCKET_NAME = 'peckwater-data'
session = boto3.Session(
    aws_access_key_id='AKIAVC3ZYDBG5UCTBKGH',
    aws_secret_access_key='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'
)

s3 = session.client('s3')
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': BUCKET_NAME, 'Key': 'IMG.jpg'},
    ExpiresIn=30
)
print(url)

# it rais the below error
# I didn't have time to fix it
# I will do it later
# <Error>
# <Code>AccessDenied</Code>
# <Message>Request has expired</Message>
# <Expires>2023-11-19T09:18:50Z</Expires>
# <ServerTime>2023-11-19T09:19:03Z</ServerTime>
# <RequestId>Y407131X191RMKST</RequestId>
# <HostId>pZW1QEYqBQDLLLfSwxzViwjHegFPffSl64HIzRF8rvcVPqZQqRUbI3JDJHP+0iNk2dAktkEdrl8=</HostId>
# </Error>