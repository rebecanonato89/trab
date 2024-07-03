import matplotlib.pyplot as plt
import os

def process_csv_and_plot():
    # Obtenha o diretório atual deste script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construa o caminho absoluto para o arquivo CSV
    csv_path = os.path.join(current_dir, '..', 'content', 'taxa_letalidade.csv')

    with open(csv_path, "r") as arquivo:
        lista_ano = []
        lista_delito = []
        lista_mortos = []

        cont = 0

        for linhas in arquivo:
            if cont > 0:
                item = linhas.split(",")
                if len(item) > 2:
                    print(f"Ano: {item[0]}")
                    print(f"Delito: {item[2]}")
                    print(f"Mortos: {item[4]}")
                    lista_ano.append(int(item[0]))
                    lista_delito.append(item[2])
                    lista_mortos.append(int(item[4]))

            cont += 1

    plt.figure(figsize=(8, 6))
    plt.plot(lista_ano, lista_mortos, marker='o', linestyle='-')
    plt.xticks(rotation=90)
    plt.xlabel('Ano')
    plt.ylabel('Mortos')
    plt.title('Homicídio por ano')
    plt.tight_layout()
    plt.grid(True)
    plt.show()