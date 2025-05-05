import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("❌ CEP não encontrado.")
        else:
            print("\nEndereço encontrado:")
            print(f"Rua: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')}")
            print(f"Estado: {dados.get('uf')}")
    else:
        print("❌ Erro ao consultar o CEP.")

if __name__ == "__main__":
    cep_input = input("Digite o CEP (apenas números): ")
    consultar_cep(cep_input.strip())
