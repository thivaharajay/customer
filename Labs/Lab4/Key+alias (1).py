import boto3

alias = 'alias/22175666'

client = boto3.client('kms', region_name='ap-southeast-2')

response = client.create_alias(AliasName=alias,TargetKeyId='arn:aws:kms:ap-southeast-2:032418238795:key/a014b039-6177-4117-abaa-313b25006fd1')
