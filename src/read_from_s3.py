# 1.load the AWS SDK
# inside aws , use cloudshell
# python3
# import boto3--> python SDK for aws

# 2.get the object from s3
# s3 = boto3.resource('s3')--> s3 resource that allows to interact with s3 API
# s3_object = s3.Bucket('peckwater-date').Object('source.txt').get()--> reading our file
# print(s3_object)

# 3.extract the content of the object
# extract only text from s3 file, without header
# text = s3_bject['Body'].read()
# print(text)



# create a new python file
# vi filename.py
# import boto3--> python SDK for aws
# s3 = boto3.resource('s3')--> s3 resource that allows to interact with s3 API
# s3_object = s3.Bucket('peckwater-date').Object('source.txt').get()--> reading our file
# text = s3_bject['Body'].read().decode()-->extract only text from s3 file, without header
# print(text)
# save the file with :wq and enter
# run the saved file with :
# python3 filename.py --> it runs your commands inside the file


import boto3
import os


session = boto3.Session(
     aws_access_key_id='AKIAVC3ZYDBG5UCTBKGH',
    aws_secret_access_key='D/romsStVlnFUSIGCIQBq9TmDS6vRwKxJrQw4AWk'
)

s3 = session.resource('s3')
obj = s3.Object('peckwater-data','time_zone.csv')
body = obj.get()['Body'].read().decode()
print(body)






