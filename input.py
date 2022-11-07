import tweepy

#Todas as chaves e valores sao fornecidos pela pagina de criação de API do twitter developers

client = tweepy.Client(bearer_token='Insire o bearer token')

client = tweepy.Client(consumer_key='Insira a consumer key',
                       consumer_secret='Insira a chave de consumer secret',
                       access_token='Access Token vai aqui',
                       access_token_secret='Access Token Secret')

response = client.create_tweet(text='Texto')

print(response)