from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def transform_silver_to_gold(df_silver, spark: SparkSession):
    """
    Função para realizar as transformações de Silver para Gold e salvar os resultados.
    
    Args:
        df_silver: DataFrame do Spark contendo os dados da camada Silver.
        spark: A SparkSession existente que será utilizada para as transformações.
        output_path: Caminho onde os dados transformados (Gold) serão salvos.
    
    Returns:
        None
    """
    # Exemplo de transformação: Definindo uma coluna "status" com base em uma condição
    df_gold = df_silver.withColumn("status", when(col("total_value") > 1000, "high_value").otherwise("low_value"))
    
    # Exemplo de filtrar e ordenar os dados para a camada Gold
    df_gold = df_gold.filter(col("status") == "high_value").orderBy(col("total_value").desc())
    
    # Salvando os dados na camada Gold
    df_gold.write.mode("overwrite").parquet(f"data/gold/")

    return df_gold

if __name__ == '__main__':

    # Testando a função de transformação de Silver para Gold diretamente
    spark = SparkSession.builder \
        .appName("Silver to Gold Transformation") \
        .getOrCreate()

    # Criando um DataFrame de exemplo (simulando dados da camada Silver)
    data = [("A", 1000, 1500, "active"),
            ("B", 500, 700, "inactive"),
            ("C", 2000, 2500, "active")]

    columns = ["category", "total_value", "avg_value", "status"]
    df_silver = spark.createDataFrame(data, columns)

    # Caminho de saída para os dados transformados
    output_path = "/data"

    # Executando a transformação
    df_gold = transform_silver_to_gold(df_silver, spark, output_path)

    # Exibindo os dados transformados
    df_gold.show()

    spark.stop()