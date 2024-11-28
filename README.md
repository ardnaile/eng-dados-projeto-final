# Pipeline de Dados: Loja de Carros

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Este projeto implementa uma pipeline de dados para uma loja de carros, utilizando tecnologias como Azure Data Lake Storage Gen 2, Databricks, e PySpark. O objetivo é extrair, carregar e transformar (ELT) dados sobre carros e clientes de um banco de dados MongoDB, processá-los e armazená-los de forma eficiente em um Data Lake para posterior análise e visualização.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

## Desenho de Arquitetura

A [arquitetura](https://www.canva.com/design/DAGWT2Nq1as/a60vcFN_nH8hjaepkPSZRA/view?utm_content=DAGWT2Nq1as&utm_campaign=designshare&utm_medium=link&utm_source=editor) da pipeline de dados está sendo desenhada e é composta pelos seguintes elementos:

* Fonte de Dados (MongoDB): Informações sobre carros e clientes são extraídas de um banco de dados MongoDB.
* Processamento de Dados (Databricks e PySpark): Utilizamos Azure Databricks para processar os dados extraídos. As transformações dos dados são feitas usando PySpark.
* Armazenamento (Azure Data Lake Storage Gen 2): Os dados processados são armazenados no Azure Data Lake para análise e consulta posterior.


## Pré-requisitos

Antes de começar, verifique se você possui os seguintes pré-requisitos instalados:

* Azure Account: Você precisará de uma conta Azure e de acesso ao Azure Data Lake Storage Gen 2.
* Databricks Account: Uma conta no Azure Databricks para execução dos notebooks Spark.
* MongoDB: Banco de dados MongoDB com as coleções de dados da loja de carros.
* PySpark: Para processar os dados de forma distribuída.

## Instalação
### 1. Configurar o MongoDB
Crie uma conta no MongoDB com as coleções de dados de carros e clientes.

### 2. Configurar o Azure Data Lake
Configure o Azure Data Lake Storage Gen 2 e crie os contêineres para armazenar os dados.

## Ferramentas utilizadas

* [MongoDB](https://www.mongodb.com/pt-br) - Banco de dados utilizado para o sistema de origem.
* [Azure Data Lake Storage Gen 2](https://azure.microsoft.com/en-us/products/storage/data-lake-storage/) - Armazenamento de dados escalável e seguro.
* [Databricks](https://www.databricks.com/br) - Plataforma de análise baseada em Apache Spark.
* [PySpark](https://spark.apache.org/docs/latest/api/python/index.html) - Biblioteca Python para trabalhar com Apache Spark.

## Colaboração
Se desejar publicar suas modificações em um repositório remoto no GitHub, siga estes passos:

1. Crie um novo repositório vazio no GitHub.
2. No terminal, navegue até o diretório raiz do projeto.
3. Execute os seguintes comandos:

```bash
git remote set-url origin https://github.com/seu-usuario/nome-do-novo-repositorio.git
git add .
git commit -m "Adicionar minhas modificações"
git push -u origin master
```

Isso configurará o repositório remoto e enviará suas modificações para lá.

## Versão

A versão atual desse projeto é a v1.0.

## Autores

* [**Eliandra Cardoso**](https://github.com/ardnaile) - *Banco MongoDB e documentação*
* [**Gustavo Valsechi**](https://github.com/gustavo-valsechi) - *Extração e transformação dos dados*
* [**Paulo Dal Ponte**](https://github.com/pauloDalponte) - *Criação do ambiente*

## Licença

Este projeto está sob a licença **MIT** - veja o arquivo [LICENSE](https://github.com/jlsilva01/projeto-ed-satc/blob/main/LICENSE) para detalhes.

## Referências

* [How To Create STUNNING Code Documentation With MkDocs Material Theme](https://www.youtube.com/watch?v=Q-YA_dA8C20)

