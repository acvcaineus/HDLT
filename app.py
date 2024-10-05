from flask import Flask, render_template, request
from calculos_dlt import classificar_dlts
from dados_dlt import DLT_OPTIONS

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', dlts=DLT_OPTIONS.keys())

# Rota para processar o cálculo
@app.route('/calcular', methods=['POST'])
def calcular():
    # Coleta os pesos do formulário
    pesos = {
        'seguranca': float(request.form['seguranca']),
        'escalabilidade': float(request.form['escalabilidade']),
        'eficiencia_energetica': float(request.form['eficiencia_energetica']),
        'governanca': float(request.form['governanca']),
        'custos': float(request.form['custos'])
    }

    # Calcula e classifica as DLTs
    dlt_classificadas = classificar_dlts(pesos)

    # Envia os resultados para a página de resultados
    return render_template('index.html', dlts=DLT_OPTIONS.keys(), resultados=dlt_classificadas)

if __name__ == "__main__":
    app.run(debug=True)
