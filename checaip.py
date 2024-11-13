import requests
import argparse
import os

def get_ip_data(ip):
    try:
        response = requests.get(f"https://internetdb.shodan.io/{ip}")
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        return response.json()  # Retorna o resultado em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao buscar o IP {ip}: {e}")
        return None

def save_to_file(ip, data):
    filename = f"{ip}.txt"
    with open(filename, 'w') as f:
        f.write(str(data))  # Salva a representação em string dos dados no arquivo
    print(f"Resultados salvos em {filename}")

def main():
    parser = argparse.ArgumentParser(description='Buscar dados de IP na API do Shodan.')
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument('-u', '--ip', type=str, help='Endereço IP a ser consultado.')
    group.add_argument('-f', '--file', type=str, help='Arquivo contendo uma lista de IPs (um por linha).')

    args = parser.parse_args()

    if args.ip:
        ip_data = get_ip_data(args.ip)
        if ip_data:
            save_to_file(args.ip, ip_data)

    if args.file:
        if os.path.isfile(args.file):
            with open(args.file, 'r') as f:
                ips = f.read().splitlines()
                for ip in ips:
                    ip_data = get_ip_data(ip)
                    if ip_data:
                        save_to_file(ip, ip_data)
        else:
            print(f"O arquivo {args.file} não foi encontrado.")

if __name__ == '__main__':
    main()