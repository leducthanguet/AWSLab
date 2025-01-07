import json
import boto3

def handler(event, context):
    
    # Tên Lambda mà bạn muốn thay đổi concurrency
    function_name = 'server-dev-triggerS3Event'  # Thay bằng tên Lambda của bạn
    
    # Giới hạn concurrency bạn muốn thiết lập
    concurrency_limit = 8  # Tăng concurrency lên 30

    # Gọi hàm điều chỉnh concurrency
    return adjust_concurrency(function_name, concurrency_limit)


def adjust_concurrency(function_name, concurrency_limit):
    # Khởi tạo client AWS Lambda
    client = boto3.client('lambda')

    try:
        response = client.get_account_settings()
        unreserved_concurrency = response['AccountLimit']['UnreservedConcurrentExecutions']
        print("unreserved_concurrency is: ", unreserved_concurrency)
        # Cập nhật concurrency cho Lambda
        response = client.put_function_concurrency(
            FunctionName=function_name,
            ReservedConcurrentExecutions=concurrency_limit
        )
        
        print("response is: ", response)
        return {
            'statusCode': 200,
            'body': f'Successfully updated concurrency to {concurrency_limit}'
        }
    except Exception as e:
        print("e is: ", e)
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
