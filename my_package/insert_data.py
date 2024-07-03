import os
import csv

def insert_data():
    # Obtenha o diretório atual deste script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construa o caminho absoluto para o arquivo CSV
    csv_path = os.path.join(current_dir, '..', 'content', 'taxa_letalidade.csv')

    # Verifica se o arquivo CSV existe
    if not os.path.isfile(csv_path):
        print(f"Arquivo {csv_path} não encontrado!")
        return

    # Solicita a entrada de dados do usuário
    ano = input("Insira o ano: ")
    regiao = input("Insira a região: ")
    delito = input("Insira o tipo de delito: ")
    contagem_delito = input("Insira a contagem do delito (deixe em branco se não houver): ")
    populacao = input("Insira a população: ")
    taxa_cem_mil_habitantes = input("Insira a taxa por 100 mil habitantes (deixe em branco se não houver): ")

    # Abre o arquivo CSV no modo de adição
    with open(csv_path, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Escreve os novos dados no arquivo CSV
        csvwriter.writerow([ano, regiao, delito, contagem_delito, populacao, taxa_cem_mil_habitantes])

    print("Dados inseridos com sucesso!")