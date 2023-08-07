#!/usr/bin/python

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'Books'

def upload_data_to_dynamodb(data):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=data)
    print('Item added to DynamoDB table:', response['ResponseMetadata']['HTTPStatusCode'])

if __name__ == "__main__":
    data_to_upload = {
        'ISBN': '1234567890',  # Primary key attribute
        'Title': 'Example Book',
        'Author': 'John Doe',
        'Year': 2023
    }

    upload_data_to_dynamodb(data_to_upload)

