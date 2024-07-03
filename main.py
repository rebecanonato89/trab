from my_package import greet
from my_package import process_csv_and_plot
from my_package import plot_bar_chart
from my_package import insert_data

def main():
    name = "World"
    greeting = greet(name)
    print(greeting)

    # Escolha a função que deseja executar
    option = input("Escolha uma opção: \n1. Processar CSV e plotar gráfico de linha\n2. Plotar gráfico de barras\n3. Inserir novos dados\nDigite o número da opção: ")

    if option == '1':
        process_csv_and_plot()
    elif option == '2':
        plot_bar_chart()
    elif option == '3':
        insert_data()
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()

