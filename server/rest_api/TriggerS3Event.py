import json
import boto3

def handler(event, context):

    # Tạo client S3
    s3_client = boto3.client('s3')

    # Thông tin bucket và object cần lấy
    bucket_name = 's3-bucket-test-07-01-2025-thangld-01'
    object_key = 'beach.jpg'

    # Lấy object
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)

    # Đọc nội dung
    print("response is: ", response)
    
    
    """ USE TRUST POLICY """
    # # STS client
    # sts_client = boto3.client('sts')

    # # Assume the S3AccessRole
    # assumed_role = sts_client.assume_role(
    #     RoleArn="arn:aws:iam::633128508833:role/s3-full-access",
    #     RoleSessionName="LambdaS3AccessSession"
    # )

    # # Extract temporary credentials
    # credentials = assumed_role['Credentials']

    # # Use temporary credentials to access S3
    # s3_client = boto3.client(
    #     's3',
    #     aws_access_key_id=credentials['AccessKeyId'],
    #     aws_secret_access_key=credentials['SecretAccessKey'],
    #     aws_session_token=credentials['SessionToken']
    # )

    # # Perform S3 GetObject operation
    # response = s3_client.get_object(
    #     Bucket="s3-bucket-test-07-01-2025-thangld-01",
    #     Key="beach.jpg"
    # )

    # print("response is: ", response)

    
    # Xử lý sự kiện từ S3
    print("S3 Event Received:", json.dumps(event, indent=2))

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        print(f"Object {object_key} was uploaded to bucket {bucket_name}.")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "S3 PUT event processed successfully!"})
    }
