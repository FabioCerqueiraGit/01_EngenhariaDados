from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.sql import SparkSession

# Iniciar sessão Spark
spark = SparkSession.builder.appName("AnaliseSentimentos").getOrCreate()

# Carregar dados processados
df = spark.read.parquet("data/processed/tweets_processed.parquet")

# Tokenização
tokenizer = Tokenizer(inputCol="clean_text", outputCol="words")
stopwords_remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")

# TF-IDF
hashing_tf = HashingTF(inputCol="filtered_words", outputCol="raw_features")
idf = IDF(inputCol="raw_features", outputCol="features")

# Modelo de regressão logística
lr = LogisticRegression(featuresCol="features", labelCol="sentiment")

# Pipeline
pipeline = Pipeline(stages=[tokenizer, stopwords_remover, hashing_tf, idf, lr])
model = pipeline.fit(df)

# Salvar modelo
model.save("models/sentiment_model")