from flask import Flask, request, jsonify

app = Flask(__name__)

solicitacoes_manutencao = []
id_counter = 1


@app.route('/solicitacoes', methods=['GET'])
def listar_solicitacoes():
    return jsonify(solicitacoes_manutencao)


@app.route('/solicitacoes', methods=['POST'])
def criar_solicitacao():
    global id_counter
    nova_solicitacao = request.get_json()
    nova_solicitacao['id'] = id_counter
    id_counter += 1
    solicitacoes_manutencao.append(nova_solicitacao)
    return f'Solicitação de manutenção com ID {nova_solicitacao["id"]} criada com sucesso', 201


@app.route('/solicitacoes/<int:id>', methods=['PUT'])
def atualizar_solicitacao(id):
    solicitacao_existente = next((s for s in solicitacoes_manutencao if s['id'] == id), None)

    if solicitacao_existente:
        dados_atualizados = request.get_json()
        solicitacao_existente.update(dados_atualizados)
        return f'Solicitação de manutenção com ID {id} atualizada com sucesso'
    else:
        return f'Solicitação de manutenção com ID {id} não encontrada', 404


@app.route('/solicitacoes/<int:id>', methods=['DELETE'])
def excluir_solicitacao(id):
    global solicitacoes_manutencao
    solicitacoes_manutencao = [s for s in solicitacoes_manutencao if s['id'] != id]

    return f'Solicitação de manutenção com ID {id} excluída com sucesso'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
