import boto3

client = boto3.client('kms', region_name='ap-southeast-2')

response = client.create_key(
			Policy="""{
                                  "Version": "2012-10-17",
                                  "Id": "key-consolepolicy-3",
                                  "Statement": [
                                    {
                                      "Sid": "Enable IAM User Permissions",
                                      "Effect": "Allow",
                                      "Principal": {
                                        "AWS": "arn:aws:iam::032418238795:root"
                                      },
                                      "Action": "kms:*",
                                      "Resource": "*"
                                    },
                                    {
                                      "Sid": "Allow access for Key Administrators",
                                      "Effect": "Allow",
                                      "Principal": {
                                        "AWS": "arn:aws:iam::032418238795:user/CITS5503/22175666@student.uwa.edu.au"
                                      },
                                      "Action": [
                                        "kms:Create*",
                                        "kms:Describe*",
                                        "kms:Enable*",
                                        "kms:List*",
                                        "kms:Put*",
                                        "kms:Update*",
                                        "kms:Revoke*",
                                        "kms:Disable*",
                                        "kms:Get*",
                                        "kms:Delete*",
                                        "kms:TagResource",
                                        "kms:UntagResource",
                                        "kms:ScheduleKeyDeletion",
                                        "kms:CancelKeyDeletion"
                                      ],
                                      "Resource": "*"
                                    },
                                    {
                                      "Sid": "Allow use of the key",
                                      "Effect": "Allow",
                                      "Principal": {
                                        "AWS": "arn:aws:iam::032418238795:user/CITS5503/22175666@student.uwa.edu.au"
                                      },
                                      "Action": [
                                        "kms:Encrypt",
                                        "kms:Decrypt",
                                        "kms:ReEncrypt*",
                                        "kms:GenerateDataKey*",
                                        "kms:DescribeKey"
                                      ],
                                      "Resource": "*"
                                    },
                                    {
                                      "Sid": "Allow attachment of persistent resources",
                                      "Effect": "Allow",
                                      "Principal": {
                                        "AWS": "arn:aws:iam::032418238795:user/CITS5503/22175666@student.uwa.edu.au"
                                      },
                                      "Action": [
                                        "kms:CreateGrant",
                                        "kms:ListGrants",
                                        "kms:RevokeGrant"
                                      ],
                                      "Resource": "*",
                                      "Condition": {
                                        "Bool": {
                                          "kms:GrantIsForAWSResource": "true"
                                        }
                                      }
                                    }
                                  ]
                                }""",
			Description='Encryption Key',
			KeyUsage='ENCRYPT_DECRYPT',
			Origin='AWS_KMS',
			)

print('Created CMK ARN:', response['KeyMetadata']['Arn'])

