import boto3

client = boto3.client('machinelearning',region_name='us-east-1')

response = client.create_evaluation(
    EvaluationId='22175666-evaluation',
    EvaluationName='22175666-evaluation',
    MLModelId='22175666-model',
    EvaluationDataSourceId='22175666-testing1'
)
