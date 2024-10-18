import boto3
import json

def lambda_handler(event, context):
    try:  
        s3 = boto3.resource('s3')
        bucket = s3.Bucket("")
        bucket.upload_file("")
        
        return {
            "statusCode": 200,
            "body": json.dumps("Imagem armazenada com sucesso!")
        }
        
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps("Erro ao fazer upload da imagem para o S3: " + e)
        }