
# 📊 ENEM 2023 - Análise de Desempenho e Desigualdades Educacionais

Este projeto tem como objetivo analisar os fatores que influenciam o desempenho dos estudantes brasileiros no ENEM 2023, com foco em desigualdades regionais, sociais e educacionais. Utilizando dados públicos do INEP, o projeto segue todas as etapas de engenharia e análise de dados até a visualização em dashboard.

## 🔧 Tecnologias e Ferramentas Utilizadas

- **Google Cloud Platform (GCP)**
  - Google Cloud Storage (Data Lake)
  - BigQuery (Data Warehouse)
- **Python 3**
  - Pandas, Pyarrow, Google Cloud libraries
- **Looker Studio** (para visualização)
- **GitHub**
- **Medium** (para publicação de insights)

## 📁 Organização do Projeto

```
📂 dados/
 ├─ microdados_enem.csv (1.8 GB)
 ├─ microdados_enem_amostra.csv (25 MB)
📂 scripts/
 ├─ csv_para_parquet.py
 ├─ ingestao_diretorio_dados_datalake.py
 ├─ gold_arquivos_parquet_bigquery.py
📂 dashboard/
 ├─ painel interativo (link abaixo)
📂 documentacao/
 ├─ artigo_word.docx
 ├─ dicionario_de_dados.ods
```

## 📈 Dashboard Interativo

Acesse o painel com os principais insights por estado, faixa etária e tipo de escola:

🔗 [Dashboard no Looker Studio](https://lookerstudio.google.com/u/0/reporting/9456f01c-897f-4b2d-90e8-b1c87b1508a4/page/EtNPF)

## 📝 Artigo Completo com Resultados e Insights

Leitura recomendada com análise das perguntas de negócio e descobertas:

🔗 [Leia no Medium](https://medium.com/@efafc/instituto-federal-do-norte-de-minas-gerais-ifnmg-a7ddf45bdfb0)

## 📌 Principais Resultados

- Alunos de escolas privadas apresentaram melhor desempenho médio em todas as áreas.
- Participantes mais jovens obtiveram melhores notas em Linguagens e Redação.
- Estados do Sul e Sudeste destacaram-se com as maiores médias.
- Alunos da Educação Especial ainda possuem desempenho inferior, apontando desafios de inclusão.

## 📂 Scripts Utilizados

1. `csv_para_parquet.py` – Conversão de CSV para arquivos Parquet
2. `ingestao_diretorio_dados_datalake.py` – Upload dos dados para o GCS
3. `gold_arquivos_parquet_bigquery.py` – Criação das tabelas analíticas no BigQuery

## 👨‍💻 Repositório do Projeto

🔗 [GitHub - trabalho-banco-dados](https://codespaces.new/ErickFFaCunha/trabalho-banco-dados)

## 👩‍🏫 Créditos

Projeto desenvolvido como parte da disciplina **Banco de Dados 2**, sob orientação da Profª Suzana Mota – IFNMG.
