from relatorio import gerar_relatorio

def test_gerar_relatorio_com_dois_itens():
    itens = [
        {"nome": "Teclado", "quantidade": 2},
        {"nome": "Mouse", "quantidade": 5}
    ]

    resultado = gerar_relatorio(itens)

    assert resultado == "Relatório Gerado: 3"
