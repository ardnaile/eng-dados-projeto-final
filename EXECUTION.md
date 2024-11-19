## Main script

- pip install -r requirements.txt
- python scripts/main_pipeline.py

## Scripts individualmente

#### Rodar a extração
python scripts/extract/extract_mongodb.py

#### Rodar a transformação Bronze → Silver
python scripts/transform/transform_bronze_to_silver.py

#### Rodar a transformação Silver → Gold
python scripts/transform/transform_silver_to_gold.py

#### Carregar para Databricks
python python scripts/load/load_to_databricks.py