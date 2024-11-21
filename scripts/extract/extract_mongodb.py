from pyspark.sql import SparkSession
from configs import mongodb_config 

def extract_from_mongodb(mongodb_config, spark: SparkSession):
    """
    Função para extrair dados do MongoDB usando uma SparkSession existente.
    
    Args:
        mongodb_config:
            connection_string: A string de conexão com o MongoDB.
            database: O nome do banco de dados no MongoDB.
            collection: O nome da coleção no MongoDB.
        spark: A SparkSession existente que será utilizada para leitura dos dados.
    
    Returns:
        DataFrame: DataFrame do Spark contendo os dados extraídos.
    """
    return spark.read \
        .format("com.mongodb.spark.sql.DefaultSource") \
        .option("uri", f"{mongodb_config.connection_string}/{mongodb_config.database}.{mongodb_config.collection}") \
        .load()

if __name__ == '__main__':

    # Testando a função de extração diretamente
    spark = SparkSession.builder \
        .appName("MongoDB Extraction") \
        .getOrCreate()

    # Executando a extração
    df_bronze = extract_from_mongodb(mongodb_config, spark)
    
    # Exibindo os dados extraídos
    df_bronze.show()

    spark.stop()