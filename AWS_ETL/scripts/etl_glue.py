import sys
import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

# Obtenção dos argumentos do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
logger = glueContext.get_logger()

# Definição de variáveis
S3_BUCKET = "meu-bucket-de-logs"  # Certifique-se de que o nome do bucket esteja correto
RAW_LOGS_PATH = f"s3://{S3_BUCKET}/data/raw_logs/"
PROCESSED_LOGS_PATH = f"s3://{S3_BUCKET}/data/processed_logs/"
REDWIFT_DB = "logs_db"
TABLE_NAME = "logs_processed"

# Lendo dados brutos do S3
raw_logs = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [RAW_LOGS_PATH]},
    format="csv",
    format_options={"withHeader": True}
)

logger.info("Dados brutos lidos com sucesso.")

# Transformação dos dados - ajuste conforme a estrutura real dos logs
processed_logs = raw_logs.apply_mapping([
    ("user_ip", "string", "user_ip", "string"),
    ("url", "string", "url", "string"),
    ("response_code", "int", "response_code", "int"),
    ("event_time", "timestamp", "event_time", "timestamp")
])

logger.info("Dados transformados com sucesso.")

# Gravando os dados transformados no Redshift
glueContext.write_dynamic_frame.to_redshift(
    frame=processed_logs,
    catalog_connection="sua_conexao_redshift",  # Essa conexão deve estar configurada no Glue
    database=REDWIFT_DB,
    table_name=TABLE_NAME,
    redshift_tmp_dir=f"s3://{S3_BUCKET}/temp/"
)

logger.info("Dados gravados com sucesso no Redshift.")
logger.info("ETL concluído com sucesso.")