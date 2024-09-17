# 100SECURITY
# Ferramenta: FIHEX - Conversor de Arquivos
# Site: www.100security.com.br/fihex
# Por: Marcos Henrique

import binascii
import os
from colorama import Fore, Style

# Limpar a Tela
def clear_screen():
    # Verifica o sistema operacional e executa o comando apropriado
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou macOS
        os.system('clear')
        
clear_screen()

# Inicializa o Colorama
from colorama import init
init(autoreset=True)

# Banner
titulo = f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}FIHEX - Conversor de Arquivos"
site = f"{Fore.WHITE}www.100security.com.br/{Style.BRIGHT}{Fore.LIGHTCYAN_EX}fihex"

# Exibe o texto com as cores e com uma nova linha entre eles
print(f"{titulo}\n{site}")


# Conversor
def binary_to_hex(input_file, output_file):
    try:
        # Lê o arquivo binário
        with open(input_file, 'rb') as file:
            binary_data = file.read()
        # Converte para hexadecimal
        hex_data = binascii.hexlify(binary_data).decode('utf-8')
        # Salva a representação hexadecimal em um arquivo de texto
        with open(output_file, 'w') as file:
            file.write(hex_data)
        print(f"Arquivo hexadecimal salvo como: {Style.BRIGHT}{Fore.LIGHTGREEN_EX}{output_file}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {Style.BRIGHT}{Fore.LIGHTRED_EX}{input_file}")
    except Exception as e:
        print(f"Erro ao converter para hexadecimal: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{e}")

def hex_to_binary(input_file, output_file):
    try:
        # Lê o arquivo hexadecimal
        with open(input_file, 'r') as file:
            hex_data = file.read()
        # Remove espaços e quebras de linha, se houver
        hex_data = hex_data.replace(" ", "").replace("\n", "")
        # Converte a representação hexadecimal de volta para binário
        binary_data = binascii.unhexlify(hex_data)
        # Salva os dados binários no arquivo de saída
        with open(output_file, 'wb') as file:
            file.write(binary_data)
        print(f"Arquivo binário salvo como: {Style.BRIGHT}{Fore.LIGHTGREEN_EX}{output_file}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {Style.BRIGHT}{Fore.LIGHTRED_EX}{input_file}")
    except binascii.Error:
        print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Erro: O arquivo hexadecimal contém dados inválidos.")
    except Exception as e:
        print(f"Erro ao converter para binário: {Style.BRIGHT}{Fore.LIGHTRED_EX}{e}")

def menu():
    while True:
        print(f"\n{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}- - - - - - - - - - M E N U - - - - - - - - - -\n")
        print(f"{Style.BRIGHT}{Fore.WHITE}1 {Style.NORMAL}{Fore.WHITE}- Converter {Fore.LIGHTCYAN_EX}Arquivo {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Hexadecimal\n")
        print(f"{Style.BRIGHT}{Fore.WHITE}2 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Hexadecimal {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Arquivo\n")
        print(f"{Style.BRIGHT}{Fore.WHITE}3 {Style.NORMAL}{Fore.WHITE}- {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}Sair\n")
        option = input("Escolha uma opção: ")

        if option == '1':
            input_file = input("Informe o nome do arquivo a ser convertido para hexadecimal (ex: imagem.png): ")
            output_file = input("Informe o nome para salvar o arquivo hexadecimal (ex: imagem.txt): ")
            binary_to_hex(input_file, output_file)
        
        elif option == '2':
            input_file = input("Informe o nome do arquivo hexadecimal (ex: imagem.txt): ")
            output_file = input("Informe o nome para salvar o arquivo convertido (ex: imagem.png): ")
            hex_to_binary(input_file, output_file)

        elif option == '3':
            print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Saindo...")
            break
        
        else:
            print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Opção inválida. Tente novamente.")

# Executa o menu
menu()
