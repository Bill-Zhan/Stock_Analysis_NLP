import boto3
import os
s3 = boto3.resource('s3',
                    aws_access_key_id="AKIA5XT4CQXZ5VD7IL7T",
                    aws_secret_access_key="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"
                    )
# Upload a new file
cwd = os.getcwd()
data = open(os.path.join(cwd, 'database/test.txt'), 'rb')
s3.Bucket('bill-stock').put_object(Key='test.txt', Body=data)
first_bucket = s3.Bucket('bill-stock')