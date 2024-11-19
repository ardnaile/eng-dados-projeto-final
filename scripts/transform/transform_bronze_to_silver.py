# scripts/transform/transform_bronze_to_silver.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date

def transform_bronze_to_silver(df_bronze, spark: SparkSession):
    """
    Função para realizar as transformações de Bronze para Silver e salvar os resultados.
    
    Args:
        df_bronze: DataFrame do Spark contendo os dados extraídos da camada Bronze.
        spark: A SparkSession existente que será utilizada para as transformações.
        output_path: Caminho onde os dados transformados (Silver) serão salvos.
    
    Returns:
        None
    """
    # Exemplo de transformação: Filtrando dados e criando novas colunas
    df_silver = df_bronze.filter(col("status") == "active")  # Filtra apenas dados ativos
    df_silver = df_silver.withColumn("processed_date", current_date())  # Adiciona a data de processamento

    # Exemplo de agregação
    df_silver = df_silver.groupBy("category").agg(
        sum("value").alias("total_value"),
        avg("value").alias("avg_value")
    )
    
    # Salvando os dados na camada Silver
    df_silver.write.mode("overwrite").parquet(f"data/silver/")

    return df_silver

if __name__ == '__main__':

    # Testando a função de transformação de Bronze para Silver diretamente
    spark = SparkSession.builder \
        .appName("Bronze to Silver Transformation") \
        .getOrCreate()

    # Criando um DataFrame de exemplo (simulando dados da camada Bronze)
    data = [("1", "Product A", 100, "active"),
            ("2", "Product B", 200, "inactive"),
            ("3", "Product C", 300, "active")]

    columns = ["id", "name", "value", "status"]
    df_bronze = spark.createDataFrame(data, columns)

    # Caminho de saída para os dados transformados
    output_path = "/data"

    # Executando a transformação
    df_silver = transform_bronze_to_silver(df_bronze, spark, output_path)

    # Exibindo os dados transformados
    df_silver.show()

    spark.stop()