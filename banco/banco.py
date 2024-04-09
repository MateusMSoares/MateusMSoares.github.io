import json

def retornarListaCampos():
    with open('banco/campos.json', 'r') as f:
        ListaCampos = json.load(f)
    return ListaCampos

def adicionarListaCampos(campo):
    # Lê os campos existentes
    with open('banco/campos.json', 'r') as f:
        campos = json.load(f)
    # Gera o próximo ID disponível
    novo_id = gerarid()
    # Adiciona o ID ao campo
    novoRegistro = {
        'id': novo_id,
        'nome': campo["nome"],
    }
    # Adiciona o novo campo
    campos['campo'].append(novoRegistro)
    # Escreve a lista atualizada de campos de volta ao arquivo
    with open('banco/campos.json', 'w') as f:
        json.dump(campos, f)

def reescreverListaCampos(lista):
    with open('banco\campos.json', 'w') as f:
        json.dump(lista, f)

def gerarid():
    # Lê a lista de campos
    with open('banco/campos.json', 'r') as f:
        campos = json.load(f)

    # Encontra o maior ID existente
    max_id = max(campo['id'] for campo in campos['campo'])

    # Retorna o próximo ID disponível
    return max_id + 1