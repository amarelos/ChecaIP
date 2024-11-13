# ChecaIP

Esta ferramenta tem sua principal função buscar dados de IP na API do Shodan.

## Utilização

Execução unica. Basta informar apenas um endereço IP.<br>
`python3 checaip.py -u 1.1.1.1`


Execução multipla. Neste caso é necessario informar um arquivo com endereços IPs.<br>
`python3 checaip.py -f ip.txt`


```
Opções:
python3 checaip.py -u <Endereço IP> 
-u, --ip	"Endereço IP a ser consultado."
-f, --file  "Arquivo contendo uma lista de IPs (um por linha)"
```
