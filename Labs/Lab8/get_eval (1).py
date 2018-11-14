import boto3

client = boto3.client('machinelearning',region_name='us-east-1')
response = client.get_evaluation(
    EvaluationId='22175666-evaluation'
)

print(response)
