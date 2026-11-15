import csv

#Só mantendo a função antiga:
def teste():
    with open("vendas.csv", "r", encoding="utf-8", newline="") as csvfile:
        leitor_csv = csv.reader(csvfile, delimiter=",")
        for linha in leitor_csv:
            print(linha)

def teste2():
    with open('vendas.csv', 'r', encoding="utf-8", newline="") as csvfile:
        leitor_csv = csv.reader(csvfile)
        next(leitor_csv, None)
        for linha in leitor_csv:
            print(f"Nome: {linha[1]} - Quantidade: {linha[3]} - Valor: R${linha[4]}")

def teste3():
    with open("vendas.csv", "r", encoding="utf-8", newline="") as csvfile:
        leitor_csv = csv.reader(csvfile, delimiter=",")
        next(leitor_csv, None)

        faturamento = 0
        for linha in leitor_csv:
            faturamento += int(linha[3]) * float(linha[4])

        print(f"Faturamento: R$ {faturamento:.2f}")

def teste4():
    with open("vendas.csv", "r", encoding="utf-8", newline="") as csvfile:
        leitor_csv = csv.reader(csvfile, delimiter=",")
        next(leitor_csv, None)
        nome = ""
        quantidade = 0
        for linha in leitor_csv:
            if int(linha[3]) > quantidade:
                quantidade = int(linha[3])
                nome = linha[1]

        print(f"Produto mais vendido foi {nome}, vendeu {quantidade} unidades.")

def teste5():
    with open("vendas.csv", "r" , encoding="utf-8", newline="") as csvfile:
        leitor_csv = csv.reader(csvfile, delimiter=",")
        next(leitor_csv, None)
        vendas = {}
        quantidade = 0
        produto_mais_vendido = ""
        maior_quantidade = 0
        for linha in leitor_csv:
            nome = linha[1]
            quantidade = int(linha[3])
            vendas[nome] = vendas.get(nome, 0) + quantidade
        for nome, quantidade in vendas.items():
            if quantidade > maior_quantidade:
                maior_quantidade = quantidade
                produto_mais_vendido = nome

        print("=== Produto Mais Vendidos ===")
        if vendas:
            print(f"Produto: {produto_mais_vendido} / Quantidade de Vendas: {maior_quantidade}")
        else:
            print("Não existem vendas registradas")


with open("vendas.csv0", "r", encoding="utf-8", newline="") as csvfile:
    leitor_csv = csv.reader(csvfile, delimiter=",")
