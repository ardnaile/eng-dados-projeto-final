from pyspark.sql import SparkSession
from extract.extract_mongodb import extract_from_mongodb
from transform.transform_bronze_to_silver import transform_bronze_to_silver
from transform.transform_silver_to_gold import transform_silver_to_gold
from load.load_to_databricks import load_to_databricks
from configs import mongodb_config 

def run_pipeline():

    # Criar uma única instância da SparkSession
    spark = SparkSession.builder \
            .appName("Main Pipeline") \
            .config("spark.sql.streaming.checkpointLocation", "/data/checkpoints/main_pipeline") \
            .getOrCreate()

    try:
        # Etapa 1: Extração de dados do MongoDB
        print("Iniciando a extração de dados...")
        df_bronze = extract_from_mongodb(mongodb_config, spark)

        # Etapa 2: Transformação de Bronze para Silver
        print("Iniciando a transformação de Bronze para Silver...")
        transform_bronze_to_silver(df_bronze, spark)

        # Etapa 3: Transformação de Silver para Gold
        print("Iniciando a transformação de Silver para Gold...")
        df_silver = spark.read.parquet("data/silver/")  # Carregar os dados da camada Silver
        transform_silver_to_gold(df_silver, spark)

        # Etapa 4: Carga no Databricks
        print("Iniciando o carregamento dos dados no Databricks...")
        df_gold = spark.read.parquet("data/gold/")  # Carregar os dados da camada Gold
        load_to_databricks(df_gold, spark)

        print("Pipeline executado com sucesso!")

    finally:
        # Fechar a SparkSession
        spark.stop()

if __name__ == '__main__':
    run_pipeline()