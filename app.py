from flask import Flask, request, jsonify, render_template
import banco.banco as banco

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('principal.html')

@app.route('/campos', methods=['POST'])
def add_campo():
    campo = request.get_json()
    banco.adicionarListaCampos(campo)
    return jsonify(campo), 201

@app.route('/campos', methods=['GET'])
def get_campos():
    return jsonify(banco.retornarListaCampos()), 200

if __name__ == '__main__':
    app.run(debug=True)