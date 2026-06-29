# Classificacao Agricultura - Crop Recommendation

Projeto de classificação aplicado a dados agrícolas para recomendar culturas a partir de variáveis de solo e clima. O notebook cobre entendimento dos dados, preparação, treinamento de modelos e interpretação com LIME.

## Objetivo

Construir e comparar modelos de classificação capazes de apoiar recomendações agrícolas com base em atributos como nutrientes do solo, temperatura, umidade, pH e chuva.

## O que o projeto demonstra

- Estrutura analítica com etapas de data understanding, EDA, preparação e modelagem.
- Uso de Pandas para exploração e tratamento de dados tabulares.
- Visualizações com Plotly para investigar padrões entre variáveis.
- Construção de pipelines de machine learning com Scikit-learn.
- Comparação de modelos como KNN, Decision Tree e Random Forest.
- Uso de LIME para explicar predições e aumentar interpretabilidade.

## Stack

- Python
- Pandas e NumPy
- Plotly
- Scikit-learn
- LIME
- Jupyter Notebook / Google Colab

## Arquivos

| Arquivo | Descrição |
| --- | --- |
| `Classificacao_Agricultura2V.ipynb` | Notebook principal com análise, preparação e modelagem. |

## Como executar

1. Abra o notebook no Google Colab ou Jupyter.
2. Disponibilize o arquivo `Crop_recommendation.csv` no caminho esperado pelo notebook ou ajuste a célula de leitura.
3. Execute as células em ordem para reproduzir a análise e o treinamento.

## Pontos fortes para portfólio

O projeto tem bom valor técnico porque mostra uma trilha completa de machine learning supervisionado, incluindo interpretabilidade. Para Engenharia de Dados Júnior, o diferencial é a organização do ciclo analítico e a preocupação com explicação de resultados.

## Limitações atuais

- O dataset não está versionado no repositório.
- O notebook depende de Google Drive, reduzindo reprodutibilidade.
- Não há arquivo de dependências nem instrução automatizada de setup.
- A lógica de preparação e treino ainda não está modularizada.

## Próximas melhorias recomendadas

- Adicionar uma pasta `data/README.md` explicando origem e schema do dataset.
- Criar `requirements.txt` com versões mínimas das bibliotecas.
- Exportar um pipeline Scikit-learn reutilizável em `src/`.
- Registrar métricas finais em tabela única, com baseline e modelo escolhido.
- Adicionar validações para schema, tipos e valores esperados.
