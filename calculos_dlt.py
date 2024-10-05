# calculos_dlt.py
from dados_dlt import DLT_OPTIONS

def calcular_pontuacao_total(dlt, pesos):
    dlt_data = DLT_OPTIONS[dlt]
    pontuacao_total = (
        pesos["seguranca"] * dlt_data["seguranca"] +
        pesos["escalabilidade"] * dlt_data["escalabilidade"] +
        pesos["eficiencia_energetica"] * dlt_data["eficiencia_energetica"] +
        pesos["governanca"] * dlt_data["governanca"] +
        pesos["custos"] * dlt_data["custos"]
    )
    return pontuacao_total

def classificar_dlts(pesos):
    pontuacoes = {}
    for dlt in DLT_OPTIONS:
        pontuacao_total = calcular_pontuacao_total(dlt, pesos)
        pontuacoes[dlt] = pontuacao_total

    dlt_classificadas = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)
    return dlt_classificadas
