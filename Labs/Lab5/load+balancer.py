import boto3
import time

def create_instances(subnet,image_id,group):

    ec2 = boto3.client('ec2')
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            group,
        ],
        SubnetId= subnet,
        KeyName='Sydney'

    )
    time.sleep(30)


    return response['Instances'][0]['InstanceId']


def target_group(client,vpc):

    response = client.create_target_group(
        Name='targetgroup',
        Protocol='HTTP',
        Port=80,
        VpcId=vpc
    )
    return response['TargetGroups'][0]['TargetGroupName'],response['TargetGroups'][0]['TargetGroupArn']

def register(client,target_arn,ec2_id1,ec2_id2):

    response = client.register_targets(
        TargetGroupArn=target_arn,
        Targets=[
            {
                'Id': ec2_id1,
            },
            {
                'Id': ec2_id2,
            },
        ],
    )

    print(response)

def load_balancer(client,subnet1,subnet2,group):
    response = client.create_load_balancer(
        Name='load balancer',
        Subnets=[
            subnet1,subnet2
        ],
        SecurityGroups=[
            group,
        ]
    )
    return response['LoadBalancers'][0]['DNSName'],response['LoadBalancers'][0]['LoadBalancerArn']

def listener(client,load_balancer_arn,target_arn):
    response = client.create_listener(
        LoadBalancerArn=load_balancer_arn,
        Protocol='HTTP',
        Port=80,
        DefaultActions=[
            {
                'Type': 'forward' ,
                'TargetGroupArn': target_arn,
            },
        ]
    )
    print response

def main():

    vpc='vpc-050bd4e7c7677cc76'
    image_id='ami-890b62b3'
    group='sg-0b6b3d452f2d17f8e'
    subnet1='subnet-02d93083aec47cb01'
    subnet2 = 'subnet-0303ebb548eabde58'


    ec2_id1 = create_instances(subnet1,image_id,group)      #ec2 instance 1
    ec2_id2 = create_instances(subnet2,image_id,group)      #ec2 instance 2

    print ec2_id1,ec2_id2

    client = boto3.client('elbv2')



    target_name,target_arn=target_group(client,vpc)         #creating target group
    print target_name,target_arn


    register(client,target_arn,ec2_id1,ec2_id2)             #registering target group


    elb_dns,load_balancer_arn=load_balancer(client,subnet1,subnet2,group)     #creating load balancer


    listener(client,load_balancer_arn,target_arn)         #creating listener

