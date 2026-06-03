import boto3

def lambda_handler(event, context):
    # Entrada
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    alumno = {
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'alumno_datos': alumno_datos
    }

    table.put_item(Item=alumno)

    # Salida
    return {
        'statusCode': 200,
        'message': 'Alumno creado correctamente',
        'alumno': alumno
    }
