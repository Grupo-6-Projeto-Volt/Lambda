import boto3
import json

def lambda_handler(event, context):
    
    nome_imagem = event['nomeImagem']
    imagem = event['imagem']
    
    try:  
        s3 = boto3.resource('s3')
        bucket = s3.Bucket("s3-02231010")
        bucket.put_object(key=nome_imagem, body=imagem)
        
        return json.dumps({
            'status': 200,
            'params': event,
            'valid': True,
            'result': 'Upload da imagem para o S3 realizado com sucesso!'
        })
        
    except Exception as e:
        return json.dumps({
            'status': 400,
            'params': event,
            'valid': False,
            'errorMessage': e
        })