import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users_sample_test')

table.put_item(
   Item={
        'username': 'johndoe',
        'last_name': 'Doe',
        'first_name': 'John',
        'age': 25,
        'account_type': 'standard_user',
    }
)