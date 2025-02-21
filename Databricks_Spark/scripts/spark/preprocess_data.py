from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import re

# Iniciar sessão Spark
spark = SparkSession.builder.appName("PreprocessamentoTweets").getOrCreate()

# Carregar dados
df = spark.read.json("data/raw/tweets_raw.json")

# Função para limpar texto
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)     # Remove menções
    text = re.sub(r"#\w+", "", text)     # Remove hashtags
    text = re.sub(r"[^\w\s]", "", text)  # Remove pontuação
    return text.strip()

# Aplicar limpeza
clean_text_udf = udf(clean_text, StringType())
df = df.withColumn("clean_text", clean_text_udf(df["text"]))

# Salvar dados processados
df.write.parquet("data/processed/tweets_processed.parquet")