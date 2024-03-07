import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Specify the table name
table_name = 'Users_sample_test'

# Get the DynamoDB table
table = dynamodb.Table(table_name)

# Define the primary key of the item you want to update
key = {
    'username': 'johndoe'
}

# Define the attributes to update
update_expression = "SET #lname = :lname, #age = :age"
expression_attribute_names = {
    "#lname": "last_name",
    "#age": "age"
}
expression_attribute_values = {
    ":lname": "UpdatedLastName",
    ":age": 26
}

# Update the item
table.update_item(
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeNames=expression_attribute_names,
    ExpressionAttributeValues=expression_attribute_values
)
