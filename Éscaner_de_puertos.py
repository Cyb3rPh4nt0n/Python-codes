#Éscaner_de_puertos.py

#IMPORTAMOS LOS MÓDULOS NECESARIOS:
import pyfiglet
import nmap
import requests
import json

#COMIENZO:
comienzo = pyfiglet.figlet_format("Éscaner de Puertos")
print(comienzo)
print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')

#DEFINICIÓN DE IP O RANGO PARA EL ESCANEO:
rango_ip = input("""\nIntroduce la dirección IP o el rango a escanear:
         * Dirección IP: 192.168.0.1
         * Rango direccones IP: 192.168.0.1-255
         * Rango dirección IP indicando máscara: 192.168.0.1/24 \n""")

resultado = []
nm = nmap.PortScanner()
print("\n\033[1;33;40mEscaneando la IP o rango",rango_ip,"por favor espere el resultado.\033[0m\n")
nm.scan(rango_ip, arguments='-sS -sV -sU -T4 -F --version-intensity 0')

print("\n\033[1;33;40mEquipos detectados | Resultados:\033[0m\n")

#LISTANDO LOS HOST:
listado_host = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
listado_activos = []

#FILTRADO POR HOSTS ACTIVOS:
for host, status in listado_host:
    if status in 'up':
        listado_activos.append(host)

#MOSTRAR (IP | HOSTNAME | PUERTOS - ESTADO Y SERVICIO):
for h in listado_activos:
    parcial = {}
    contador = 0
    print('\033[0;30;47mIP: {}\033[0m'.format(h))
    parcial.update({"IP":(h)})
    if nm[h].hostname() == '':
        print('No se obtuvo el hostname.')
        parcial.update({"hostname":"No se obtuvo el host name."})
    else:
        print('Hostname: {}'.format(nm[h].hostname()))
        parcial.update({"hostname":nm[h].hostname()})
    print('- - - - - - - - - - - - - - - - - - - - - - - -')
    if nm[h].all_protocols() == []:
        print('\033[1;31;40m\n- no se detectó ningún protocolo -\033[0m')
        parcial.update({'Escaneo':'No se detectó ningún protocolo'})
    for proto in nm[h].all_protocols():
        try:
            
            print('\033[1;32;40mProtocolo: {proto}\033[0m'.format(proto=proto.upper()))
            lport = nm[h][proto].keys()
            for port in lport:
                contador += 1
                print('Puerto: %s\tEstado: %s\tServicio: %s - %s' % (port, nm[h][proto][port]['state'], nm[h][proto][port]['name'], nm[h][proto][port]['product']))
                parcial.update({'Puerto ' + proto.upper() + ' ' + str(contador):{'Puerto':port, 'Estado':nm[h][proto][port]['state'], 'Servicio': nm[h][proto][port]['product']}})
        except Exception as e:
            print('Ocurrió un error al escanear uno de los host, ver detalle:', e)
    print('\n = = = = = = = = = = = = = = = = = = = = = = = = = =\n')
    resultado.append(parcial)

print('. . . . . . . . . . . . . . . . . . . . . . . . .\n')
print("\n\033[1;36,40mFin del escaneo.\033[0m\n")

#SIMULAR EL POST DE LA VARIABLE RESULTADO A UN SERVIDOR:
try:
	requests.post('http://127.0.0.1/example/fake_url.php', json=resultado, timeout=5)
except:
    print("Enviando resultados a la url \033[0;30;47mhttp://127.0.0.1/example/fake_url.php\033[0m. . . . \033[1;31;40m[FAIL]\033[0m")

#Convertimos la variable en un archivo JSON y guardamos en el equipo:
with open("resultado_nmap.json", "w") as f:
    json.dump(resultado, f)
print("Guardando el archivo \033[0;30;47mresultado_nmap.JSON\033[0m. . . . \033[1;32;40m[OK]\033[0m")