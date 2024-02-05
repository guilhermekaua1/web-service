import requests

def fazer_chamada_get(url):
    response = requests.get(url)
    return response.json()


def fazer_chamada_post(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response.text


def fazer_chamada_put(url, id, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'{url}/{id}', json=data, headers=headers)
    return response.text


def fazer_chamada_delete(url, id):
    response = requests.delete(f'{url}/{id}')
    return response.text


if __name__ == '__main__':
    url_servidor = 'http://localhost:8080/solicitacoes'

    while True:
        print("\nEscolha uma opção:")
        print("1. Listar solicitações")
        print("2. Criar uma nova solicitação")
        print("3. Atualizar uma solicitação")
        print("4. Excluir uma solicitação")
        print("5. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            lista_solicitacoes = fazer_chamada_get(url_servidor)
            print(f'\nLista de Solicitações: {lista_solicitacoes}')

        elif opcao == '2':
            descricao = input("Digite a descrição da solicitação: ")
            prioridade = input("Digite a prioridade da solicitação: ")
            nova_solicitacao = {'descricao': descricao, 'prioridade': prioridade}
            resposta_criacao = fazer_chamada_post(url_servidor, nova_solicitacao)
            print(f'Resposta do Servidor (Criação): {resposta_criacao}')

        elif opcao == '3':
            id_atualizacao = int(input("Digite o ID da solicitação a ser atualizada: "))
            dados_atualizados = {'status': input("Digite o novo status da solicitação: ")}
            resposta_atualizacao = fazer_chamada_put(url_servidor, id_atualizacao, dados_atualizados)
            print(f'Resposta de Atualização: {resposta_atualizacao}')

        elif opcao == '4':
            id_exclusao = int(input("Digite o ID da solicitação a ser excluída: "))
            resposta_exclusao = fazer_chamada_delete(url_servidor, id_exclusao)
            print(f'Resposta de Exclusão: {resposta_exclusao}')

        elif opcao == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")
