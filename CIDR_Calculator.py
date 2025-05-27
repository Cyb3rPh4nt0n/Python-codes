#Calculator CIDR.py

#LISTAS
CIDR_Class = {
  1:"128.0.0.0",
  2:"192.0.0.0",
  3:"224.0.0.0",
  4:"240.0.0.0",
  5:"248.0.0.0",
  6:"252.0.0.0",
  7:"254.0.0.0",
  8:"255.0.0.0",
  9:"255.128.0.0",
  10:"255.192.0.0",
  11:"255.224.0.0",
  12:"255.240.0.0",
  13:"255.248.0.0",
  14:"255.252.0.0",
  15:"255.254.0.0",
  16:"255.255.0.0",
  17:"255.255.128.0",
  18:"255.255.192.0",
  19:"255.255.224.0",
  20:"255.255.240.0",
  21:"255.255.248.0",
  22:"255.255.252.0",
  23:"255.255.254.0",
  24:"255.255.255.0",
  25:"255.255.255.128",
  26:"255.255.255.192",
  27:"255.255.255.224",
  28:"255.255.255.240",
  29:"255.255.255.248",
  30:"255.255.255.252",
  31:"255.255.255.254",
  32:"255.255.255.255",
}

#INICIO
print("[+] Bienvenido a la calculadora CIDR")
IP_Address = str(input("[+] Ingresa la dirección IP -> "))
separar = IP_Address.split("/")
IP = separar[0]
CIDR = separar[1]
print(f"[+] La IP es {IP} y el CIDR es {CIDR}\n")

#CALCULAR MÁSCARA DE RED
CIDR = int(CIDR)
if (CIDR <= 8) & (CIDR >= 1):
  print("[+] La dirección IP ingresada pertenece a la clase 0")
elif (CIDR <= 16) & (CIDR > 8):
  print("[+] La dirección IP ingresada pertenece a la clase A")
elif (CIDR <= 24) & (CIDR > 16):
  print("[+] La dirección IP ingresada pertenece a la clase B")
elif (CIDR <= 32) & (CIDR > 24):
  print("[+] La dirección IP ingresada pertenece a la clase C")
else:
  print("[!] La dirección IP ingresada no es correcta, inténtelo de nuevo")
  exit()
mascara_red = CIDR_Class[CIDR]
print(f"[+] La máscara de red es {mascara_red}")

#CALCULAR TOTAL HOSTS
bits_0 = (32 - CIDR)
operacion_total_hosts = ((2 ** bits_0) - 2)
if (operacion_total_hosts <= 0):
  operacion_total_hosts = 0
print(f"[+] El total hosts es {operacion_total_hosts}")

#CALCULAR NETWORK ID
IP_octeto = IP.split(".")
IP_octeto_1 = IP_octeto[0]
IP_octeto_1 = int(IP_octeto_1)
IP_octeto_2 = IP_octeto[1]
IP_octeto_2 = int(IP_octeto_2)
IP_octeto_3 = IP_octeto[2]
IP_octeto_3 = int(IP_octeto_3)
IP_octeto_4 = IP_octeto[3]
IP_octeto_4 = int(IP_octeto_4)

Mask_octeto = mascara_red.split(".")
Mask_octeto_1 = Mask_octeto[0]
Mask_octeto_1 = int(Mask_octeto_1)
Mask_octeto_2 = Mask_octeto[1]
Mask_octeto_2 = int(Mask_octeto_2)
Mask_octeto_3 = Mask_octeto[2]
Mask_octeto_3 = int(Mask_octeto_3)
Mask_octeto_4 = Mask_octeto[3]
Mask_octeto_4 = int(Mask_octeto_4)

operacion_1 = (IP_octeto_1 & Mask_octeto_1)
operacion_2 = (IP_octeto_2 & Mask_octeto_2)
operacion_3 = (IP_octeto_3 & Mask_octeto_3)
operacion_4 = (IP_octeto_4 & Mask_octeto_4)
operacion_1 = str(operacion_1)
operacion_2 = str(operacion_2)
operacion_3 = str(operacion_3)
operacion_4 = str(operacion_4)

network_id = f"{operacion_1}.{operacion_2}.{operacion_3}.{operacion_4}"
print(f"[+] El network ID es {network_id}")

#CALCULAR BROADCAST ADDRESS
bits_0 = int(bits_0)
if bits_0 <= 0:
  bits_0 = 1

IP_octeto_1 = bin(IP_octeto_1)[2:]
IP_octeto_1 = IP_octeto_1.rjust(8, '0')
#print(IP_octeto_1)

IP_octeto_2 = bin(IP_octeto_2)[2:]
IP_octeto_2 = IP_octeto_2.rjust(8, '0')
#print(IP_octeto_2)

IP_octeto_3 = bin(IP_octeto_3)[2:]
IP_octeto_3 = IP_octeto_3.rjust(8, '0')
#print(IP_octeto_3)

IP_octeto_4 = bin(IP_octeto_4)[2:]
IP_octeto_4 = IP_octeto_4.rjust(8, '0')
#print(IP_octeto_4)

IP_binario = f"{IP_octeto_1}.{IP_octeto_2}.{IP_octeto_3}.{IP_octeto_4}"
#print(IP_binario)
IP_binario = list(IP_binario)

if bits_0 == 1:
  IP_binario[-1] = 1
elif bits_0 == 2:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
elif bits_0 == 3:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
elif bits_0 == 4:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
elif bits_0 == 5:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
elif bits_0 == 6:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
elif bits_0 == 7:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
elif bits_0 == 8:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
elif bits_0 == 9:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
elif bits_0 == 10:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
elif bits_0 == 11:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
elif bits_0 == 12:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
elif bits_0 == 13:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
elif bits_0 == 14:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
elif bits_0 == 15:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
elif bits_0 == 16:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
elif bits_0 == 17:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
elif bits_0 == 18:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
elif bits_0 == 19:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
elif bits_0 == 20:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
elif bits_0 == 21:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
elif bits_0 == 22:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
elif bits_0 == 23:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
elif bits_0 == 24:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
elif bits_0 == 25:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
elif bits_0 == 26:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
  IP_binario[-29] = 1
elif bits_0 == 27:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
  IP_binario[-29] = 1
  IP_binario[-30] = 1
elif bits_0 == 28:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
  IP_binario[-29] = 1
  IP_binario[-30] = 1
  IP_binario[-31] = 1
elif bits_0 == 29:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
  IP_binario[-29] = 1
  IP_binario[-30] = 1
  IP_binario[-31] = 1
  IP_binario[-32] = 1
elif bits_0 == 30:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
  IP_binario[-29] = 1
  IP_binario[-30] = 1
  IP_binario[-31] = 1
  IP_binario[-32] = 1
  IP_binario[-33] = 1
elif bits_0 == 31:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
  IP_binario[-29] = 1
  IP_binario[-30] = 1
  IP_binario[-31] = 1
  IP_binario[-32] = 1
  IP_binario[-33] = 1
  IP_binario[-34] = 1
elif bits_0 == 32:
  IP_binario[-1] = 1
  IP_binario[-2] = 1
  IP_binario[-3] = 1
  IP_binario[-4] = 1
  IP_binario[-5] = 1
  IP_binario[-6] = 1
  IP_binario[-7] = 1
  IP_binario[-8] = 1
  IP_binario[-10] = 1
  IP_binario[-11] = 1
  IP_binario[-12] = 1
  IP_binario[-13] = 1
  IP_binario[-14] = 1
  IP_binario[-15] = 1
  IP_binario[-16] = 1
  IP_binario[-17] = 1
  IP_binario[-19] = 1
  IP_binario[-20] = 1
  IP_binario[-21] = 1
  IP_binario[-22] = 1
  IP_binario[-23] = 1
  IP_binario[-24] = 1
  IP_binario[-25] = 1
  IP_binario[-26] = 1
  IP_binario[-28] = 1
  IP_binario[-29] = 1
  IP_binario[-30] = 1
  IP_binario[-31] = 1
  IP_binario[-32] = 1
  IP_binario[-33] = 1
  IP_binario[-34] = 1
  IP_binario[-35] = 1

IP_binario = str(IP_binario)
#print(IP_binario)
IP_binario = IP_binario.replace("'", "")
IP_binario = IP_binario.replace("[", "")
IP_binario = IP_binario.replace("]", "")
IP_binario = IP_binario.replace(",", "")
#print(IP_binario)
IP_binario = IP_binario.split(".")

IP_octeto_1 = IP_binario[0]
#print(IP_octeto_1)

bit1_octeto1 = int(IP_octeto_1[0])
if bit1_octeto1 == 1:
  Operacion1_octeto1 = (2 ** 7)
else:
  Operacion1_octeto1 = 0

bit2_octeto1 = int(IP_octeto_1[2])
if bit2_octeto1 == 1:
  Operacion2_octeto1 = (2 ** 6)
else:
  Operacion2_octeto1 = 0

bit3_octeto1 = int(IP_octeto_1[4])
if bit3_octeto1 == 1:
  Operacion3_octeto1 = (2 ** 5)
else:
  Operacion3_octeto1 = 0

bit4_octeto1 = int(IP_octeto_1[6])
if bit4_octeto1 == 1:
  Operacion4_octeto1 = (2 ** 4)
else:
  Operacion4_octeto1 = 0

bit5_octeto1 = int(IP_octeto_1[8])
if bit5_octeto1 == 1:
  Operacion5_octeto1 = (2 ** 3)
else:
  Operacion5_octeto1 = 0

bit6_octeto1 = int(IP_octeto_1[10])
if bit6_octeto1 == 1:
  Operacion6_octeto1 = (2 ** 2)
else:
  Operacion6_octeto1 = 0

bit7_octeto1 = int(IP_octeto_1[12])
if bit7_octeto1 == 1:
  Operacion7_octeto1 = (2 ** 1)
else:
  Operacion7_octeto1 = 0

bit8_octeto1 = int(IP_octeto_1[14])
if bit8_octeto1 == 1:
  Operacion8_octeto1 = (2 ** 0)
else:
  Operacion8_octeto1 = 0

Resultado_octeto_1 = (Operacion1_octeto1 + Operacion2_octeto1 + Operacion3_octeto1 + Operacion4_octeto1 + Operacion5_octeto1 + Operacion6_octeto1 + Operacion7_octeto1 + Operacion8_octeto1)
#print(f"[+] EL RESULTADO DEL PRIMER OCTETO ES DE {Resultado_octeto_1}")

IP_octeto_2 = IP_binario[1]
#print(IP_octeto_2)

bit1_octeto2 = int(IP_octeto_2[1])
if bit1_octeto2 == 1:
  Operacion1_octeto2 = (2 ** 7)
else:
  Operacion1_octeto2 = 0

bit2_octeto2 = int(IP_octeto_2[3])
if bit2_octeto2 == 1:
  Operacion2_octeto2 = (2 ** 6)
else:
  Operacion2_octeto2 = 0

bit3_octeto2 = int(IP_octeto_2[5])
if bit3_octeto2 == 1:
  Operacion3_octeto2 = (2 ** 5)
else:
  Operacion3_octeto2 = 0

bit4_octeto2 = int(IP_octeto_2[7])
if bit4_octeto2 == 1:
  Operacion4_octeto2 = (2 ** 4)
else:
  Operacion4_octeto2 = 0

bit5_octeto2 = int(IP_octeto_2[9])
if bit5_octeto2 == 1:
  Operacion5_octeto2 = (2 ** 3)
else:
  Operacion5_octeto2 = 0

bit6_octeto2 = int(IP_octeto_2[11])
if bit6_octeto2 == 1:
  Operacion6_octeto2 = (2 ** 2)
else:
  Operacion6_octeto2 = 0

bit7_octeto2 = int(IP_octeto_2[13])
if bit7_octeto2 == 1:
  Operacion7_octeto2 = (2 ** 1)
else:
  Operacion7_octeto2 = 0

bit8_octeto2 = int(IP_octeto_2[15])
if bit8_octeto2 == 1:
  Operacion8_octeto2 = (2 ** 0)
else:
  Operacion8_octeto2 = 0

Resultado_octeto_2 = (Operacion1_octeto2 + Operacion2_octeto2 + Operacion3_octeto2 + Operacion4_octeto2 + Operacion5_octeto2 + Operacion6_octeto2 + Operacion7_octeto2 + Operacion8_octeto2)
#print(f"[+] EL RESULTADO DEL SEGUNDO OCTETO ES DE {Resultado_octeto_2}")

IP_octeto_3 = IP_binario[2]
#print(IP_octeto_3)

bit1_octeto3 = int(IP_octeto_3[1])
if bit1_octeto3 == 1:
  Operacion1_octeto3 = (2 ** 7)
else:
  Operacion1_octeto3 = 0

bit2_octeto3 = int(IP_octeto_3[3])
if bit2_octeto3 == 1:
  Operacion2_octeto3 = (2 ** 6)
else:
  Operacion2_octeto3 = 0

bit3_octeto3 = int(IP_octeto_3[5])
if bit3_octeto3 == 1:
  Operacion3_octeto3 = (2 ** 5)
else:
  Operacion3_octeto3 = 0

bit4_octeto3 = int(IP_octeto_3[7])
if bit4_octeto3 == 1:
  Operacion4_octeto3 = (2 ** 4)
else:
  Operacion4_octeto3 = 0

bit5_octeto3 = int(IP_octeto_3[9])
if bit5_octeto3 == 1:
  Operacion5_octeto3 = (2 ** 3)
else:
  Operacion5_octeto3 = 0

bit6_octeto3 = int(IP_octeto_3[11])
if bit6_octeto3 == 1:
  Operacion6_octeto3 = (2 ** 2)
else:
  Operacion6_octeto3 = 0

bit7_octeto3 = int(IP_octeto_3[13])
if bit7_octeto3 == 1:
  Operacion7_octeto3 = (2 ** 1)
else:
  Operacion7_octeto3 = 0

bit8_octeto3 = int(IP_octeto_3[15])
if bit8_octeto3 == 1:
  Operacion8_octeto3 = (2 ** 0)
else:
  Operacion8_octeto3 = 0

Resultado_octeto_3 = (Operacion1_octeto3 + Operacion2_octeto3 + Operacion3_octeto3 + Operacion4_octeto3 + Operacion5_octeto3 + Operacion6_octeto3 + Operacion7_octeto3 + Operacion8_octeto3)
#print(f"[+] EL RESULTADO DEL TERCER OCTETO ES DE {Resultado_octeto_3}")

IP_octeto_4 = IP_binario[3]
#print(IP_octeto_4)

bit1_octeto4 = int(IP_octeto_4[1])
if bit1_octeto4 == 1:
  Operacion1_octeto4 = (2 ** 7)
else:
  Operacion1_octeto4 = 0

bit2_octeto4 = int(IP_octeto_4[3])
if bit2_octeto4 == 1:
  Operacion2_octeto4 = (2 ** 6)
else:
  Operacion2_octeto4 = 0

bit3_octeto4 = int(IP_octeto_4[5])
if bit3_octeto4 == 1:
  Operacion3_octeto4 = (2 ** 5)
else:
  Operacion3_octeto4 = 0

bit4_octeto4 = int(IP_octeto_4[7])
if bit4_octeto4 == 1:
  Operacion4_octeto4 = (2 ** 4)
else:
  Operacion4_octeto4 = 0

bit5_octeto4 = int(IP_octeto_4[9])
if bit5_octeto4 == 1:
  Operacion5_octeto4 = (2 ** 3)
else:
  Operacion5_octeto4 = 0

bit6_octeto4 = int(IP_octeto_4[11])
if bit6_octeto4 == 1:
  Operacion6_octeto4 = (2 ** 2)
else:
  Operacion6_octeto4 = 0

bit7_octeto4 = int(IP_octeto_4[13])
if bit7_octeto4 == 1:
  Operacion7_octeto4 = (2 ** 1)
else:
  Operacion7_octeto4 = 0

bit8_octeto4 = int(IP_octeto_4[15])
if bit8_octeto4 == 1:
  Operacion8_octeto4 = (2 ** 0)
else:
  Operacion8_octeto4 = 0

Resultado_octeto_4 = (Operacion1_octeto4 + Operacion2_octeto4 + Operacion3_octeto4 + Operacion4_octeto4 + Operacion5_octeto4 + Operacion6_octeto4 + Operacion7_octeto4 + Operacion8_octeto4)
#print(f"[+] EL RESULTADO DEL CUARTO OCTETO ES DE {Resultado_octeto_4}")

Broadcast_address = f"{Resultado_octeto_1}.{Resultado_octeto_2}.{Resultado_octeto_3}.{Resultado_octeto_4}"
print(f"[+] La Broadcast Address es {Broadcast_address}")