
import boto3
import json

s3 = boto3.client('s3')

bucket_name = '22175666-cloudstorage'

bucket_policy = {
	"Version": "2012-10-17",
	"Statement": {
		"Sid": "AllowAllS3ActionsInUserFolderForUserOnly",
		"Effect": "Deny",
		"Principal": "*",
		"Action": "s3:*",
		"Resource": ["arn:aws:s3:::22175666-cloudstorage",
				"arn:aws:s3:::22175666-cloudstorage/*"
		 ],
		"Condition": {
			"StringNotLike": {
				"aws:username": "22175666@student.uwa.edu.au"
			}
		}
	}
}

bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
