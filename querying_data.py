import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users_sample_test')


response = table.get_item(
    Key={
        'username': 'johndoe',
        'last_name': 'Doe'
    }
)

item = response['Item']
print(item)