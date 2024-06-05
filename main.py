import matplotlib.pyplot as plt
import os

# Dicionário para temperatura da superfície da água de regiões específicas do país
regions = [
    {"name": "sul", "max": 22, "min": 14},
    {"name": "sudeste", "max": 25, "min": 22},
    {"name": "nordeste", "max": 30, "min": 26},
    {"name": "norte", "max": 32, "min": 27}
]

#Função para limpar o terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para checar se é um número ou não
def check_number(prompt):
    number = input(prompt)
    while not number.isnumeric():
        number = input("Digite apenas números: ")
    number = float(number)
    return number

# Função para coletar entradas do usuário
def collect_data(data_type):
    data = []
    days = check_number("Digite o número de dias em que se realizaram coleta de dados: ")
    days = int(days)
    for day in range(1, days + 1):  
        entry = check_number(f"Digite o valor de {data_type} para o dia {day}: ")
        if data_type == "ph":
            while entry > 12 or entry < 0:
                entry = check_number(f"Digite o valor de {data_type}, em um intervalo válido(0 a 12), para o dia {day}: ")
        data.append(entry)
    return data

# Função para calcular a média dos valores
def calculate_average(data):
    return sum(data) / len(data)

# Função para plotar dados
def plot_data(data, data_type):
    days = list(range(1, len(data) + 1)) 
    average_value = calculate_average(data) 
    
    plt.figure(figsize=(10, 5))
    plt.bar(days, data, color='blue', alpha=0.7, label=f'{data_type.capitalize()}')
    plt.axhline(y=average_value, color='r', linestyle='--', label=f'Média de {data_type.capitalize()}')
    plt.xlabel('Dia')
    plt.ylabel(data_type.capitalize())
    plt.title(f'{data_type.capitalize()} ao Longo dos Dias')
    plt.legend()
    plt.grid(True)
    print(f"\nMédia de {data_type}: {average_value}\n")
    plt.show(block=False)
    print("\n Lembre-se de chechar os valores obtidos\n")

# Função para checar região
def check_region(prompt):
    region = input(prompt).lower()
    while region not in ["nordeste", "sul", "sudeste", "norte"]:
        region = input("\nDigite uma região litorânea brasileira válida: ")
    for i in range(len(regions)):
        if region == regions[i]["name"]:
            return regions[i]["min"], regions[i]["max"]

# Função para consultar dados
def consult(data_type):
    # Consultar PH
    if data_type == "ph":
        value = check_number(f"Digite o valor de {data_type} coletado, apenas números entre 0 e 12: ")
        while value > 12 or value < 0:
            value = check_number("Digite apenas valores entre 0 e 12: ")
        if value > 8.5:
            return ("\nO valor de pH está acima do normal. "
                    "Isso pode indicar alta alcalinidade, que pode ser perigosa para a vida marinha, "
                    "causando estresse aos organismos e afetando a biodiversidade. "
                    "Possíveis causas incluem poluição por resíduos industriais ou esgoto.")
        elif value < 7:
            return ("\nO valor de pH está abaixo do normal. "
                    "Isso pode indicar alta acidez, que pode corroer conchas e esqueletos de organismos marinhos, "
                    "afetar a saúde dos peixes e outras formas de vida marinha. "
                    "Possíveis causas incluem chuva ácida, poluição industrial ou agrícola.")
        else:
            return "\nO valor de pH está dentro do padrão."

    # Consultar temperatura
    if data_type == "temperatura":
        value = check_number(f"Digite a {data_type} coletada no local: ")
        min_value, max_value = check_region(f"Digite a região na qual a coleta da {data_type} foi realizada: ")
        if value > max_value:
            return ("\nO valor de temperatura está acima do normal para a região escolhida. "
                    "Temperaturas elevadas podem causar estresse térmico nos organismos marinhos, "
                    "resultando em branqueamento de corais e afetando a saúde de várias espécies. "
                    "Possíveis causas incluem mudanças climáticas e aquecimento global.")
        elif value < min_value:
            return ("\nO valor de temperatura está abaixo do normal para a região escolhida. "
                    "Temperaturas muito baixas podem também estressar os organismos marinhos, "
                    "afetando sua capacidade de sobrevivência e reprodução. "
                    "Possíveis causas incluem mudanças climáticas e correntes frias anômalas.")
        else:
            return "\nO valor de temperatura está dentro dos padrões da região."

# Menu principal
def main():
    while True:
        print("Bem-vindo ao Sistema de Monitoramento Blue Ocean\n")
        choice = input("Digite 'gerar' para gerar uma análise detalhada com base no número de dias escolhidos por você, ou tecle qualquer outra coisa para consultar um valor: ")
        
        if choice.lower() == "gerar":
            while True:
                data_type = input("Escolha o tipo de dado para inserir (ph, temperatura, nível do mar) ou 'sair' para finalizar: ").lower()
                if data_type == 'sair':
                    break  # Sai do loop se o usuário digitar 'sair'
                elif data_type in ['ph', 'temperatura', 'nível do mar']:
                    data = collect_data(data_type)  # Coleta os dados do usuário
                    plot_data(data, data_type)  # Plota os dados coletados
                    break
                else:
                    print("Tipo inválido. Por favor, escolha entre 'ph', 'temperatura' ou 'nível do mar'.")
        
        else:
            while True:
                data_type = input("Escolha o tipo de valor que quer consultar (ph ou temperatura): ").lower()
                if data_type in ['ph', 'temperatura']:
                    print(consult(data_type))
                    break
                else:
                    print("Tipo inválido. Por favor, escolha entre 'ph' ou 'temperatura'.")
        
        keep_going = input("Digite [N] para encerrar ou qualquer outra tecla para realizar mais uma verificação: ").lower()
        
        if keep_going.lower() == "n":
            clear()
            print("Programa encerrado")
            break
        else:
            clear()
            print("Continuando...\n")

# Executa o menu principal
main()
