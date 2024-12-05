# Pipeline de Dados: Loja de Carros

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Este projeto implementa uma pipeline de dados para uma loja de carros, utilizando tecnologias como Azure Data Lake Storage Gen 2, Databricks, e PySpark. O objetivo é extrair, carregar e transformar (ELT) dados de um banco de dados MongoDB, processá-los e armazená-los de forma eficiente em um Data Lake para posterior análise e visualização.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte a [DOCUMENTAÇÃO](https://ardnaile.github.io/eng-dados-projeto-final/) para mais detalhes sobre como o projeto foi feito!

## Desenho de Arquitetura

![image](https://github.com/user-attachments/assets/44dbaa39-e8f4-45a5-bf40-d30b81b2f704)

* Fonte de Dados (MongoDB): Informações sobre carros, clientes, funcionários, pagamentos, vendas e serviços são extraídas de um banco de dados MongoDB.
* Processamento de Dados (Databricks e PySpark): Foi utilizado o Azure Databricks para processar os dados extraídos. As transformações dos dados são feitas usando PySpark.
* Armazenamento (Azure Data Lake Storage Gen 2): Os dados processados são armazenados no Azure Data Lake para análise e consulta posterior.


## Pré-requisitos

Antes de começar, verifique se você possui os pré-requisitos:

* Azure Account: Você precisará de uma conta Azure e de acesso ao Azure Data Lake Storage Gen 2.
* MongoDB: Banco de dados MongoDB com as coleções de dados da loja de carros.

Consulte a [DOCUMENTAÇÃO](https://ardnaile.github.io/eng-dados-projeto-final/pre-requisitos/) para mais detalhes.

## Ferramentas utilizadas

* [MongoDB](https://www.mongodb.com/pt-br) - Banco de dados utilizado para o sistema de origem.
* [Terraform](https://www.terraform.io/) - IaC (Infrastructure as Code) para configuração do Azure e Databricks.
* [Azure Data Lake Storage Gen 2](https://azure.microsoft.com/en-us/products/storage/data-lake-storage/) - Armazenamento de dados escalável e seguro.
* [Databricks](https://www.databricks.com/br) - Plataforma de análise baseada em Apache Spark.
* [PySpark](https://spark.apache.org/docs/latest/api/python/index.html) - Biblioteca Python para trabalhar com Apache Spark.
* [MKDocs](https://www.mkdocs.org/) - Documentação

## Colaboração
Se você deseja contribuir para o projeto, siga os passos abaixo para clonar o repositório, criar uma branch e enviar suas alterações.

### 1. Clonar o repositório

Para começar a contribuir, clone o repositório na sua máquina local:

```
git clone https://github.com/ardnaile/eng-dados-projeto-final.git
```

### 2. Criar um branch para suas alterações
Antes de começar a fazer alterações, crie uma nova branch. Isso mantém o fluxo de trabalho organizado e facilita o controle de mudanças.

```
git checkout -b minha-branch
```

### 3. Fazer alterações
Agora, faça as alterações necessárias no código, documentação ou outros arquivos.

### 4. Comitar suas alterações
Depois de realizar as modificações, adicione os arquivos alterados ao stage e faça um commit:

```
git add .
git commit -m "Descrição das minhas alterações"
```

### 5. Enviar suas alterações
Após o commit, envie suas alterações para repositório remoto:

```
git push origin minha-branch
```

### 6. Criar um Pull Request
Vá até o repositório original no GitHub e crie um Pull Request com suas alterações. Descreva claramente o que foi alterado e o motivo da alteração.

### 7. Revisão e Merge
A equipe do projeto revisará suas alterações. Se tudo estiver correto, as alterações serão integradas ao repositório principal.

## Versão

A versão atual desse projeto é a v1.0.

## Autores

* [**Eliandra Cardoso**](https://github.com/ardnaile) - *Banco MongoDB e documentação*
* [**Gustavo Valsechi**](https://github.com/gustavo-valsechi) - *Extração e transformação dos dados*
* [**Paulo Dal Ponte**](https://github.com/pauloDalponte) - *Criação do ambiente e dashboard*

## Licença

Este projeto está sob a licença **MIT** - veja o arquivo [LICENSE](https://github.com/jlsilva01/projeto-ed-satc/blob/main/LICENSE) para detalhes.

## Referências

* [How To Create STUNNING Code Documentation With MkDocs Material Theme](https://www.youtube.com/watch?v=Q-YA_dA8C20) - vídeo referência para a documentação com MKDocs
* [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture) - referência para o desenho da arquitetura
* [Car Sales Report](https://www.kaggle.com/datasets/missionjee/car-sales-report) - referência para a criação do banco de dados de origem

