iV
import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Launch an EC2 instance
response = ec2.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Example Amazon Linux AMI ID, replace with your own
    InstanceType='t2.micro',           # Instance type (t2.micro is eligible for free tier)
    MinCount=1,                        # Minimum number of instances to launch
    MaxCount=2,                        # Maximum number of instances to launch
    KeyName='aws devops',           # Replace with your EC2 key pair name
)

# Print the instance ID of the newly launched EC2 instance
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance {instance_id} launched successfully.")

