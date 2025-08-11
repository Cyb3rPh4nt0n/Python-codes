# NetRecon.py by Cyb3rPh4nt0n

#########################################################
#####            Importaciones de Módulos           #####
#########################################################

import nmap, requests, getmac, subprocess, socket, re
from concurrent.futures import ThreadPoolExecutor

#########################################################
#####                  Colores                      #####
#########################################################

BlackColour = "\033[0;30m"
RedColour = "\033[0;31m"
GreenColour = "\033[0;32m"
BlueColour = "\033[0;34m"
PurpleColour = "\033[0;35m"
YellowColour = "\033[1;33m"
EndColour = "\033[0m"

#########################################################
#####                     Input                     #####
#########################################################

ip = input(f"{YellowColour}[+]{EndColour} {BlueColour}Ingrese la dirección IP y el prefijo CIDR ->{EndColour} ")
print(f"{PurpleColour}-------------------------------------------------------------------------------------------------------------------------{EndColour}\n")

#########################################################
#####     Escanear Red en Busca de Dispositivos     #####
#########################################################

def escanear_red(ip):
  scanner = nmap.PortScanner()

  scanner.scan(hosts=ip, arguments='-sn')

  dispositivos = []

  for host in scanner.all_hosts():
    if scanner[host]['status']['state'] == 'up':
      ip = host
      dispositivos.append(ip)
  return dispositivos

lista_de_dispositivos=escanear_red(ip)
print(f"{YellowColour}[+]{EndColour} {BlueColour}Dispositivos activos:{EndColour} {GreenColour}{lista_de_dispositivos}{EndColour}")

#######################################################
#####    Sacar Direcciones MAC de Dispositivos    #####
#######################################################

def obtener_direccion_mac(lista_de_dispositivos):

  lista_direcciones_mac = []
  for ip in lista_de_dispositivos:
    mac = getmac.get_mac_address(ip=ip)
    lista_direcciones_mac.append(mac)
  return lista_direcciones_mac

direcciones_mac = obtener_direccion_mac(lista_de_dispositivos)
print(f"{YellowColour}[+]{EndColour} {BlueColour}Direcciones MAC ->{EndColour} {GreenColour}{direcciones_mac}{EndColour}")

######################################################
#####       Obtener IP pública de la Red         #####
######################################################

def obtener_ip_publica(url):
  response = requests.get(url)
  ip_address = response.text
  return ip_address

url = "https://api.ipify.org"
ip_publica = obtener_ip_publica(url)
print(f"{YellowColour}[+]{EndColour} {BlueColour}La IP pública es ->{EndColour} {GreenColour}{ip_publica}{EndColour}")

#####################################################
#####      Obtener S.O de los dispositivos      #####
#####################################################

def obtener_OS(lista_de_dispositivos):
  for dispositivo in lista_de_dispositivos:
    resultado = subprocess.run(['ping', '-n', '1', f'{dispositivo}'], capture_output=True, text=True)
    match = re.search(r'ttl[=|:](\d+)', resultado.stdout, re.IGNORECASE)
    ttl = int(match.group(1)) if match else None
    if ttl == 128:
      print(f"{YellowColour}[+]{EndColour} {BlueColour}El dispositivo{EndColour} {GreenColour}{dispositivo}{EndColour} {BlueColour}tiene un SO Windows.{EndColour}")
    if ttl == 64:
      print(f"{YellowColour}[+]{EndColour} {BlueColour}El dispositivo{EndColour} {GreenColour}{dispositivo}{EndColour} {BlueColour}tiene un SO Linux.{EndColour}")

Sistema_Operativo = obtener_OS(lista_de_dispositivos)

#####################################################
##### Escanear Puertos Abiertos de Dispositivos #####
#####################################################

def scan_ports(dispositivo, port):

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.250)
  result = sock.connect_ex((dispositivo, port))
  sock.close()
  if result == 0:
    return port

def port_scan(lista_de_dispositivos):
  
  for dispositivo in lista_de_dispositivos:
    print(f"\n{YellowColour}[+]{EndColour}{BlueColour} Escaneando la IP{EndColour}{GreenColour} {dispositivo}{EndColour}{BlueColour}:{EndColour}")
    with ThreadPoolExecutor(max_workers=200) as executor:
      futures = [executor.submit(scan_ports, dispositivo, port) for port in range(1, 65536)]
      for f in futures:
        port = f.result()
        if port:
          print(f"\t{YellowColour}[+]{EndColour}{BlueColour} Puerto{EndColour} {PurpleColour}{port}{EndColour}{GreenColour} ABIERTO{EndColour}")

puertos_abiertos = port_scan(lista_de_dispositivos)