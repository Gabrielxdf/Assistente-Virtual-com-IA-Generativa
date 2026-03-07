# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `6-melhores-investimentos.pdf` | PDF | Explica os 6 melhores tipos de investimentos e seus objetivos |
| `Mapa-Investidor-de-Verdade.pdf` | PDF | Indica os 3 primeiros passos para se começar a investir na metodologia de verdade, que usa a abordagem fundamentalista |
| `carteira de verdade.txt` | TXT | Carteira de investimentos planejada utilizando a metodologia de verdade, descrevendo os 6 tipos de investimentos e o objetivo de cada um |
| `Tabela-criterios-REITs.xlsx` | XLSX | Os fundamentos para escolher um Reit |
| `Tabela-criterios-Stocks-1.xlsx` | XLSX | Os fundamentos para escolher um Stock |
| `Tabela-fundamentos-FIIs.pdf` | PDF | Os fundamentos para escolher um Fundo de Investimento Imobiliário (Fii) |
| `Tabela-fundamentos-acoes.pdf` | PDF | Os fundamentos para escolher uma ação na bolsa |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Estratégia de Integração

### Como os dados são carregados?

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json
import pdfplumber

# ============ CARREGAR DADOS ============
with pdfplumber.open('./data/6-melhores-investimentos.pdf') as pdf:
    melhores_investimentos = "\n".join(page.extract_text() for page in pdf.pages)

with pdfplumber.open('./data/Mapa-Investidor-de-Verdade.pdf') as pdf:
    mapa_investidor = "\n".join(page.extract_text() for page in pdf.pages)

with pdfplumber.open('./data/Tabela-fundamentos-acoes.pdf') as pdf:
    fundamentos_acoes = "\n".join(page.extract_text() for page in pdf.pages)

with pdfplumber.open('./data/Tabela-fundamentos-FIIs.pdf') as pdf:
    fundamentos_fiis = "\n".join(page.extract_text() for page in pdf.pages)

carteira = pd.read_csv('./data/carteira de verdade.txt', sep=None, engine='python')
fundamentos_reits = pd.read_excel('./data/Tabela-criterios-REITs.xlsx')
fundamentos_stocks = pd.read_excel('./data/Tabela-criterios-Stocks-1.xlsx')
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

TODO
[Sua descrição aqui]

---

## Exemplo de Contexto Montado

TODO
> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
