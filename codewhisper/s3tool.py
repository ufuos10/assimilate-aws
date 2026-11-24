#!/usr/bin/env python

# build a function that returns all of the buckets in my s3 account
# import boto3

# def list_s3_buckets():
#     # Create a session using your AWS credentials
#     session = boto3.Session(
#         aws_access_key_id='YOUR_ACCESS_KEY',
#         aws_secret_access_key='YOUR_SECRET_KEY',
#         region_name='YOUR_REGION'
#     )
#     # Create an S3 client
#     s3_client = session.client('s3')
#     # List all buckets
#     response = s3_client.list_buckets()
#     # Extract bucket names from the response
#     bucket_names = [bucket['Name'] for bucket in response['Buckets']]
#     return bucket_names

import boto3

def list_s3_buckets():
    s3_client = boto3.client("s3")   # picks up credentials automatically
    response = s3_client.list_buckets()
    return [bucket["Name"] for bucket in response["Buckets"]]

if __name__ == "__main__":
    print(list_s3_buckets())