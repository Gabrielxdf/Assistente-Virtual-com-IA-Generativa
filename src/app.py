import pandas as pd
import pdfplumber
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

# ============ FUNÇÃO PARA LER PDF ============
def ler_pdf(caminho):
    texto = []
    with pdfplumber.open(caminho) as pdf:
        for page in pdf.pages:
            conteudo = page.extract_text()
            if conteudo:
                texto.append(conteudo)
    return "\n".join(texto)

# ============ CARREGAR DADOS ============
melhores_investimentos = ler_pdf('./data/6-melhores-investimentos.pdf')
mapa_investidor = ler_pdf('./data/Mapa-Investidor-de-Verdade.pdf')
fundamentos_acoes = ler_pdf('./data/Tabela-fundamentos-acoes.pdf')
fundamentos_fiis = ler_pdf('./data/Tabela-fundamentos-FIIs.pdf')

with open('./data/carteira de verdade.txt', 'r', encoding='utf-8') as f:
    carteira = f.read()

fundamentos_reits = pd.read_excel('./data/Tabela-criterios-REITs.xlsx').to_string()
fundamentos_stocks = pd.read_excel('./data/Tabela-criterios-Stocks-1.xlsx').to_string()

# ============ MONTAR CONTEXTO ============
contexto = f"""
Mapa do investidor: {mapa_investidor}
Melhores investimentos: {melhores_investimentos}
Quais investimentos devem existir na carteira: {carteira}
Fundamentos para escolher ações: {fundamentos_acoes}
Fundamentos para escolher fiis: {fundamentos_fiis}
Fundamentos para escolher stocks: {fundamentos_stocks}
Fundamentos para escolher reits: {fundamentos_reits}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """
Vocé é o Fundamental, um agente financeiro inteligente especializado em investimentos utilizando a metologia de verdade, que usa a abordagem fundamentalista para escolher ações.
Seu objetivo principal é ensinar conceitos sobre investimentos seguros de forma simples para pessoas leigas ou experientes.

REGRAS:
- Recomende ações, fiis, stocks ou reits para investir com base nos fundamentos aprendidos no contexto.
- Sempre direcione o usuário com os princípios fundamentalistas, ensinando-o a escolher suas próprias ações, fiis, stocks ou reits.
- JAMAIS responda a perguntas fora do contexto de ensino sobre investimentos. Diga que responde perguntas apenas sobre investimentos e afins.
- Sempre baseie suas respostas nos dados fornecidos.
- Nunca invente informações.
- Se não souber algo, admita que não tem essa informação e ofereça alternativas como pesquisar no Google. Se a pergunta foi fora do contexto de investimentos diga que responde perguntas apenas sobre essa área.
- Use linguagem simples e tente fazer analogias.
- Sempre pergunte no final usando gatilhos para continuar a conversa com o usuário.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.title("🎓 Fundamental, o educador de investimentos fundamentais")

if pergunta := st.chat_input("Sua dúvida sobre investimentos..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
