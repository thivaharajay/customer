import boto3

client = boto3.client('machinelearning', region_name='us-east-1')

response = client.create_ml_model(
    MLModelId='22175666-model',
    MLModelName='22175666-model',
    MLModelType='BINARY',
    TrainingDataSourceId='22175666-training1',
)
