import boto3

def lambda_handler(event, context):
    # Entrada
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    alumno = response.get('Item')

    if alumno is None:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }

    # Salida
    return {
        'statusCode': 200,
        'alumno': alumno
    }
