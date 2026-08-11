import boto3

def lambda_handler(event, context):

    ec2 = boto3.client(
        "ec2",
        region_name="ap-south-1"
    )

    instance_id = "YOUR_INSTANCE_ID"

    print(f"Restarting instance {instance_id}")

    ec2.reboot_instances(
        InstanceIds=[instance_id]
    )

    print("Restart command sent successfully")

    return {
        "statusCode": 200,
        "body": "EC2 restart initiated."
    }