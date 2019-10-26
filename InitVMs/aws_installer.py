import boto3


if __name__ == '__main__':

    ec2 = boto3.resource('ec2')
    # key = ec2.KeyPair('net4ukey')
    instances = ec2.create_instances(
        ImageId='ami-08f0c33d35b3c9ddb',
        MinCount=1,
        MaxCount=1,
        KeyName='net4ukey',
        InstanceType="t2.micro",
        NetworkInterfaces=[{
            "DeviceIndex": 0,
            "SubnetId": 'subnet-0924711b1c1e40fcc',
            "AssociatePublicIpAddress": True,
        }]
    )
