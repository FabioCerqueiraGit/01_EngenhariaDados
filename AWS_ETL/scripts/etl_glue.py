import sys
import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
logger = glueContext.get_logger()

# Lendo dados brutos do S3
raw_logs = glueContext.create_dynamic_frame.from_catalog(database="sua_database", table_name="sua_tabela_raw_logs")

# Transformação dos dados
processed_logs = raw_logs.apply_mapping([("coluna1", "string", "coluna1", "string"), 
                                           ("coluna2", "string", "coluna2", "string")])

# Gravando os dados transformados no S3
glueContext.write_dynamic_frame.to_redshift(frame=processed_logs, 
                                              catalog_connection="sua_conexao_redshift", 
                                              database="sua_database_redshift", 
                                              table_name="logs_processed", 
                                              redshift_tmp_dir="s3://nome-do-seu-bucket/temp/")

logger.info("ETL concluído com sucesso.")