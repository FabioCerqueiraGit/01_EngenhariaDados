from tweepy import API, OAuthHandler
import json

# Configurações da API do Twitter
consumer_key = "SUA_CONSUMER_KEY"
consumer_secret = "SUA_CONSUMER_SECRET"
access_token = "SEU_ACCESS_TOKEN"
access_token_secret = "SEU_ACCESS_TOKEN_SECRET"

# Autenticação
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

# Extrair tweets
tweets = api.search(q="databricks", lang="pt", count=100)

# Salvar em JSON
with open("data/raw/tweets_raw.json", "w") as f:
    json.dump([tweet._json for tweet in tweets], f)