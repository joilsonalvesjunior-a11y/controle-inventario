def cadastrar_item(nome, quantidade):
    if not nome.strip(): raise ValueError("Nome obrigatório")
    if quantidade < 0: raise ValueError("Quantidade inválida")
    return {"nome": nome, "quantidade": quantidade}
