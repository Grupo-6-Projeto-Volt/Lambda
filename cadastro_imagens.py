import boto3

def lambda_handler(event, context):
    
    nome_imagem = event['nomeImagem']
    imagem = event['imagem']
    
    try:  
        s3 = boto3.resource('s3')
        bucket = s3.Bucket("s3-02231010")
        bucket.put_object(key=nome_imagem, body=imagem)
        
        return {
            'status': 200,
            'params': event,
            'valid': True,
            'result': 'Upload da imagem para o S3 realizado com sucesso!'
        }
        
    except Exception as e:
        return {
            'status': 400,
            'params': event,
            'valid': True,
            'result': "Erro ao fazer upload da imagem para o S3: " + e
        }