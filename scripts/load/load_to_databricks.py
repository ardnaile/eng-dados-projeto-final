from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

def load_to_databricks(df: DataFrame, spark: SparkSession):
    """
    Função para carregar os dados no Databricks no formato Parquet.
    
    Args:
        df: DataFrame com os dados a serem carregados.
        output_path: Caminho de destino no Databricks (DBFS ou outro sistema de arquivos).
        spark: SparkSession, que será usada para executar a gravação dos dados.
    
    Returns:
        None
    """
    # Salvando o DataFrame em formato Parquet no caminho especificado
    df.write.mode("overwrite").parquet("/data/gold/final_analytics")
    print(f"Dados carregados no Databricks em '/data/gold/final_analytics' no formato Parquet.")
    
if __name__ == '__main__':

    # Testando a função de carregamento diretamente
    spark = SparkSession.builder \
        .appName("Load to Databricks") \
        .getOrCreate()

    # Criando um DataFrame de exemplo (simulando dados da camada Gold)
    data = [("A", 1500, 2000, "high_value"),
            ("B", 2500, 3000, "high_value"),
            ("C", 1200, 1500, "high_value")]

    columns = ["category", "total_value", "avg_value", "status"]
    df_gold = spark.createDataFrame(data, columns)

    # Caminho de saída no Databricks File System (DBFS) para armazenar os dados em Parquet
    output_path = "/data/gold/final_analytics"

    # Chamando a função para carregar os dados
    load_to_databricks(df_gold, output_path, spark)

    spark.stop()