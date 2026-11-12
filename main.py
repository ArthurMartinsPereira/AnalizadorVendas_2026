import csv

with open("vendas.csv", "r", encoding="utf-8", newline="") as csvfile:
    leitor_csv = csv.reader(csvfile, delimiter=",")
    for linha in leitor_csv:
        print(linha)
