# TCE10988 - Aprendizado de Máquina
## Manutenção Preditiva
###### Aluno: Yago de Rezende dos Santos

---

### Objetivo
O projeto tem como objetivo o desenvolvimento de um modelo de aprendizado de máquina com a finalidade de
indicar se um equipamento tem uma probabilidade alta de falhar em um determinado período de tempo. 
O modelo é treinado com base em dados fornecidos pelo professor (cliente), contendo informações
de identificação dos equipamentos, idade, dados de sensores, além de registros e classificação de falhas.

---

### Características do Código
O código é desenvolvido em Python e utiliza as seguintes bibliotecas (primariamente):
- pandas
- numpy
- seaborn (matplotlib)
- sklearn
- juptyer notebook

___Para uma lista completa de bibliotecas, verifique o arquivo `requirements.txt`___

---

### Execução do Código
Para executar o código, é necessário ter o Python instalado na máquina.
Siga os passos abaixo para a instalação do ambiente e execução do código:
```bash
# Instalação do ambiente
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Execução do código
python main.py --input=<caminho_do_arquivo_csv> --output=<caminho_do_arquivo_csv> --action=<mean>
```

---

### Acompanhamento do Projeto
O projeto está em desenvolvimento e ainda não foi finalizado. A previsão de entrega é de 7 semanas partindo do dia 02/04/2024.
O cronograma planejado contém as seguintes atividades:

- [x] Revisão de programação em Python:\
  * 4 horas (uma semana)
- [ ] **Conceitos de processamento de dados e codificação**:
  * 8 horas (duas semanas)
- [ ] Modelos de Machine Learning para regressão e codificação:
  * 12 horas (três semanas)
- [ ] Modelos de Machine Learning para classificação e codificação:
  * 8 horas (duas semanas)
- [ ] Técnicas de pós-processamento e codificação:
  * 4 horas (uma semana)
- [ ] Avaliação da solução:
  * 8 horas (duas semanas)
- [ ] Documentação final da solução e apresentação
  * 8 horas (duas semanas)

---

### Extras
> Detalhes extras de implementação e entrega do projeto final

#### Documentação
A documentação do projeto está disponível no diretório `docs` e contém informações sobre o projeto, código e resultados obtidos.

#### Detalhes do Projeto
O projeto é organizado de forma que o arquivo `main.py` seja o ponto de entrada do código. Porém,
o código foi modularizado e organizado em diretórios para facilitar a manutenção e entendimento geral. O projeto
segue boas práticas de programação sobre o paradigma POO (utilizando diretrizes como DRY, KISS, SOLID, etc.). 
Além disso, o código também disponibiliza um arquivo jupyter notebook para visualização
dos dados e resultados obtidos. Essa escolha tem como objetivo ampliar os recursos de visualização, facilitando a análise 
dos dados e dos resultados obtidos (vide `data_analysis.ipynb`).

#### Repositório: https://github.com/yagorezende/PredictiveMaintenance