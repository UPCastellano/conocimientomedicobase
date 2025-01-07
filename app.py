from flask import Flask, render_template, request

app = Flask(__name__)

# Base de conocimiento simple
diagnosticos = {
    "fiebre": "Puede ser un signo de infección.",
    "tos": "Puede ser un síntoma de resfriado o gripe.",
    "dolor de cabeza": "Puede ser causado por estrés o deshidratación."
   
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnostico', methods=['POST'])
def diagnostico():
    sintomas = request.form.get('sintomas')
    resultado = diagnosticos.get(sintomas.lower(), "Síntoma no encontrado.")
    return render_template('result.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)