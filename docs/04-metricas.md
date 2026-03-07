# Avaliação e Métricas


## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

Aqui, utilizarei apenas os testes estrturados.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar os melhores tipos de investimento |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o método ensinado na base de conhecimento? | Sugerir os tipos de investimento de acordo com o método de verdade utilizando a abordagem fundamentalista para escolher ativos |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de conceito
- **Pergunta:** "Quais os melhores investimentos?"
- **Resposta esperada:** "Tesouro Selic, IPCA+, Ações, Fiis, Stocks e Reits..." (baseado no `6-melhores-investimentos.pdf`)
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de ação para investir
- **Pergunta:** "Qual ação você recomenda para mim?"
- **Resposta esperada:** "Recomendo essa ação porque ela tem esses fundamentos..."
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de investimentos
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto vale a ação WEGE3 na B3?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

<!--
## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]
-->
