import mlflow
import mlflow.spark
from pyspark.sql import SparkSession

# Iniciar sessão Spark
spark = SparkSession.builder.appName("MLflowLogging").getOrCreate()

# Carregar modelo
from pyspark.ml import PipelineModel
model = PipelineModel.load("models/sentiment_model")

# Log do modelo no MLflow
mlflow.set_experiment("AnaliseSentimentos")
with mlflow.start_run():
    mlflow.spark.log_model(model, "sentiment_model")
    mlflow.log_param("algorithm", "LogisticRegression")
    mlflow.log_metric("accuracy", 0.85)  # Exemplo de métrica