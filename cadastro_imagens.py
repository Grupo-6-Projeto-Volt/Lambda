import boto3
import base64

def lambda_handler(event, context):
    
    nome_imagem = event['nomeImagem']
    imagem = event['imagem']
    
    try:  

        s3 = boto3.client('s3')

        bucket = "bucket2-ichiban" 
        zone = s3.get_bucket_location(Bucket=bucket)["LocationConstraint"] 

        zone = zone if zone != None else 'us-east-1'

        imagem = imagem[str(imagem).find(',') + 1:]

        message_bytes = base64.b64decode(imagem.encode("ascii"))

        s3.put_object(Bucket=bucket, Key=nome_imagem, Body=message_bytes)
        
        return {
            'status': 200,
            'params': event,
            'valid': True,
            'response': f'https://{bucket}.s3.{zone}.amazonaws.com/{nome_imagem}',
            'result': 'Upload da imagem para o S3 realizado com sucesso!'
        }
    except Exception as e:
        return {
            'status': 400,
            'params': event,
            'valid': False,
            'response': '',
            'result': f'Erro ao fazer upload da imagem para a S3: {str(e)}'
        }