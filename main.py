import csv

#Só mantendo a função antiga:
def teste():
    with open("vendas.csv", "r", encoding="utf-8", newline="") as csvfile:
        leitor_csv = csv.reader(csvfile, delimiter=",")
        for linha in leitor_csv:
            print(linha)

with open('vendas.csv', 'r', encoding="utf-8", newline="") as csvfile:
    leitor_csv = csv.reader(csvfile)
    next(leitor_csv, None)
    for linha in leitor_csv:
        print(f"Nome: {linha[1]} - Quantidade: {linha[3]} - Valor: R${linha[4]}")