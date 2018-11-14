import boto3
import json

attributes = []
attribute = { "fieldName": "age", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "job", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "marital", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "education", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "default", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "housing", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "loan", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "contact", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "month", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "day_of_week", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "duration", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "campaign", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "pdays", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "previous", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "poutcome", "fieldType": "CATEGORICAL" }
attributes.append(attribute)
attribute = { "fieldName": "empvarrate", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "conspriceidx", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "consconfidx", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "euribor3m", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "nremployed", "fieldType": "NUMERIC" }
attributes.append(attribute)
attribute = { "fieldName": "y", "fieldType": "BINARY" }
attributes.append(attribute)


dataSchema = {}
dataSchema['version'] = '1.0'
dataSchema['dataFormat'] = 'CSV'
dataSchema['attributes'] = attributes
dataSchema["targetFieldName"] = "y"
dataSchema["dataFileContainsHeader"] = True
json_data = json.dumps(dataSchema)

client = boto3.client('machinelearning',region_name='us-east-1')
response = client.create_data_source_from_s3(
            DataSourceId='22175666-testing1',
            DataSourceName='22175666-testing1',
            DataSpec={
                'DataLocationS3': 's3://22175666-cloudstorage/banking.csv',
                'DataSchema': json_data,
		'DataRearrangement': '''{
                                         "splitting": {
                                                            "percentBegin": 70,
                                                            "percentEnd": 100
                                                          }
                                                }''',

            },
            ComputeStatistics=True
            )
print(response)
