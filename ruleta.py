#ruleta.py

import random

initial_money = int(input("¿Con cuánto dinero desea jugar? -> "))
technique = str(input("¿Qué técnica desea utilizar (martingala/inverseLabrouchere/fibonacci/D_Alembert)? -> "))

def helpPanel():
  print("[+] Uso: ")
  print("\t-Indicar el dinero con el que se quiere jugar.")
  print("\t-Indicar la técnica que se desea emplear.")

def martingala():
  print(f"[+] Tiene {initial_money}€ y va ha utilizar la técnica {technique}.")
  initial_bet = int(input("¿Cuánto dinero quiere apostar? -> "))
  par_impar = str(input("¿A qué quieres apostar continuamente (par/impar)? -> "))
  print(f"[+] Va ha apostar {initial_bet}€ a {par_impar}.")

  backup_bet=initial_bet
  money=initial_money
  play_counter=1
  jugadas_malas="[ "
  max_money=0

  while True:
    money=(money-initial_bet)
    print(f"\n[+] Has apostado {initial_bet}€ y te quedas con {money}€")
    random_number=(random.randint(0,36))
    print(f"[+] Ha salido el número {random_number}")
    play_counter+=1

    if (money > 0):
      if (par_impar=="par"):
        if (random_number % 2 == 0):
          if (random_number == 0):
            print("[+] Ha salido el 0, por lo tanto pierdes")
            initial_bet=(initial_bet * 2)
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Ahora mismo te quedas en {money}€")
          else:
            print("[+] El número es par, por lo tanto ganas")
            reward=(initial_bet * 2)
            print(f"[+] Ganas un total de  {reward}€")
            money=(money+reward)
            if (money > max_money):
              max_money=money
            print(f"[+] Tienes {money}€")
            initial_bet=backup_bet
        else:
          print("[+] El número es impar, por lo tanto pierdes")
          initial_bet=(initial_bet * 2)
          jugadas_malas+=str(f"{random_number} ")
          print(f"[+] Ahora mismo te quedas en {money}€")
      else:
        if (random_number % 2 == 0):
          if (random_number == 0):
            print("[+] Ha salido el 0, por lo tanto pierdes")
            initial_bet=(initial_bet *2 )
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Ahora mismo te quedas en {money}€")
          else:
            print("[+] El número es par, por lo tanto pierdes")
            initial_bet=(initial_bet * 2)
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Ahora mismo te quedas en {money}€")
        else:
          print("[+] El número es impar, por lo tanto ganas")
          reward=(initial_bet * 2)
          print(f"[+] Ganas un total de {reward}€")
          money=(money+reward)
          if (money > max_money):
            max_money=money
          print(f"[+] Tienes {money}€")
          initial_bet=backup_bet
    else:
      #Te quedas sin dinero
      print("[+] Te has quedado sin dinero cabrón")
      break
  print(f"[+] Ha habido un total de {play_counter} jugadas.")
  print(f"[+] A continuación se van a representar los números que no te favorecián: {jugadas_malas}]")
  print(f"[+] El máximo de dinero que has logrado tener es de {max_money}€")

def inverseLabrouchere():
  print(f"[+] Tiene {initial_money}€ y va ha utilizar la técnica {technique}.")
  par_impar = str(input("¿A qué quieres apostar continuamente (par/impar)? -> "))
  print(f"[+] Va ha jugar con un objetivo de ganacia de 10€ a {par_impar}.")

  money=initial_money
  initial_sequence=[1, 2, 3, 4]
  sequence=initial_sequence
  play_counter=1
  jugadas_malas="[ "
  max_money=0
#  print(sequence)

  while True:
    try:
      sequence=list(sequence)
      operador_1=(sequence[0])
      operador_2=(sequence[-1])
      bet=(operador_1+operador_2)
      money=(money-bet)
      print(f"\n[+] Has apostado {bet}€ y te quedas con {money}€")
      random_number=(random.randint(0,36))
      print(f"[+] Ha salido el número {random_number}")
      play_counter+=1

      if (money > 0):
        if (par_impar == "par"):
          if (random_number % 2 == 0):
            if (random_number == 0):
              print("[+] Ha salido el cero, por lo tanto pierdes")
              del sequence[0]
              del sequence[-1]
              jugadas_malas+=str(f"{random_number} ")
              print(f"[+] Ahora mismo te quedas en {money}€")
            else:
              print("[+] Ha salido par, por lo tanto ganas")
              reward=(bet * 2)
              print(f"[+] Ganas un total de {reward}€")
              money=(money+reward)
              if (money > max_money):
                max_money=money
              print(f"[+] Tienes {money}€")
              sequence.append(bet)
          else:
            print("[+] El número es impar por lo tanto pierdes")
            del sequence[0]
            del sequence[-1]
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Ahora mismo te quedas en {money}€")
          print
        else:
          if (random_number % 2 == 0):
            if (random_number == 0):
              print("[+] Ha salido el cero, por lo tanto pierdes")
              del sequence[0]
              del sequence[-1]
              jugadas_malas+=str(f"{random_number} ")
              print(f"[+] Ahora mismo te quedas en {money}€")
            else:
              print("[+] Ha salido par, por lo tanto pierdes")
              del sequence[0]
              del sequence[-1]
              jugadas_malas+=str(f"{random_number} ")
              print(f"[+] Ahora mismo te quedas en {money}€")
          else:
            print("[+] El número es impar por lo tanto ganas")
            reward=(bet * 2)
            print(f"[+] Ganas un total de {reward}€")
            money=(money+reward)
            if (money > max_money):
              max_money=money
            print(f"[+] Tienes {money}€")
            sequence.append(bet)     
      else:
        print("[+] Te has quedado sin dinero cabrón")
        break
    except Exception as e:
      sequence=list(initial_sequence)
  print(f"[+] Ha habido un total de {play_counter} jugadas.")
  print(f"[+] A continuación se van a representar los números que no te favorecián: {jugadas_malas}]")
  print(f"[+] El máximo de dinero que has logrado tener es de {max_money}€")

def fibonacci():
  print(f"[+] Vas a jugar con {initial_money}€ y la técnica {technique}")
  par_impar=str(input("¿A qué deseas apostar continuamente (par/impar)? -> "))

  money=initial_money
  sequence=[1, 1]
  initial_bet=0
  play_counter=1
  jugadas_malas="[ "
  max_money=0

  while True:
    sequence=list(sequence)
    operator_1=(sequence[-1])
    operator_2=(sequence[-2])
    append=(operator_1+operator_2)
    bet=(sequence[initial_bet])
    money=(money-bet)
    print(f"\n[+] Se va ha apostar {bet}€ a {par_impar}, te quedas con {money}€")
    random_number=(random.randint(0,36))
    print(f"[+] Ha salido el número {random_number}")
    play_counter+=1

    if (money > 0):
      if (par_impar=="par"):
        if (random_number % 2 == 0):
          if (random_number == 0):
            print("[+] Ha salido el 0, por lo tanto pierdes")
            sequence.append(append)
            initial_bet+=1
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Te quedas en {money}€")
          else:
            print("[+] Ha salido par, por lo tanto ganas")
            reward=(bet * 2)
            print(f"[+] Has ganado {reward}€")
            money=(money+reward)
            if (money > max_money):
              max_money=money
            if (initial_bet >= 2):
              initial_bet-=2
            else:
              initial_bet=0
        else:
          print("[+] Ha salido impar, por lo tanto pierdes")
          sequence.append(append)
          initial_bet+=1
          jugadas_malas+=str(f"{random_number} ")
          print(f"[+] Te quedas en {money}€")
      else:
        if (random_number % 2 == 0):
          if (random_number == 0):
            print("[+] Ha salido 0, por lo tanto pierdes")
            sequence.append(append)
            initial_bet+=1
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Te quedas en {money}€")
          else:
            print("[+] Ha salido par, por lo tanto pierdes")
            sequence.append(append)
            initial_bet+=1
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Te quedas en {money}€")
        else:
          print("[+] Ha salido impar, por lo tanto ganas")
          reward=(bet * 2)
          print(f"[+] Has ganado {reward}€")
          money=(money+reward)
          if (money > max_money):
            max_money=money
          if (initial_bet >= 2):
            initial_bet-=2
          else:
            initial_bet=0
    else:
      print("[+] Te has quedado sin dinero cabrón")
      break
  print(f"[+] Ha habido un total de {play_counter} jugadas.")
  print(f"[+] A continuación se van a representar los números que no te favorecián: {jugadas_malas}]")
  print(f"[+] El máximo de dinero que has logrado tener es de {max_money}€")

def D_Alembert():
  print(f"[+] Vas a jugar con {initial_money}€ y a utilizar la técnica de {technique}")
  bet=int(input("¿Con cuánto dinero quiere empezar a apostar? -> "))
  par_impar=str(input("¿A qué desea apostar continuamente (par/impar)? -> "))
  
  money=initial_money
  play_counter=1
  jugadas_malas="[ "
  max_money=0

  while True:
    money=(money-bet)
    print(f"\n[+] Has apostado {bet}€ a {par_impar} y te quedas con {money}")
    random_number=(random.randint(0,36))
    print(f"[+] Ha salido el número {random_number}")
    play_counter+=1
   
    if (money > 0):
      if (par_impar=="par"):
        if (random_number % 2 == 0):
          if (random_number == 0):
            print("[+] Ha salido el 0, por lo tanto pierdes")
            bet+=1
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Te quedas en {money}€")
          else:
            print("[+] Ha salido par, por lo tanto ganas")
            reward=(bet * 2)
            print(f"[+] Has ganado {reward}€")
            money=(money+reward)
            if (money > max_money):
              max_money=money
            print(f"[+] Ahora tienes {money}€")
            if (bet >= 11):
              bet-=1
            else:
              bet=10
        else:
          print("[+] Ha salido impar, por lo tanto pierdes")
          bet+=1
          jugadas_malas+=str(f"{random_number} ")
          print(f"[+] Te quedas en {money}€")
      else:
        if (random_number % 2 == 0):
          if (random_number == 0):
            print("[+] Ha salido el 0, por lo tanto pierdes")
            bet+=1
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Te quedas en {money}€")
          else:
            print("[+] Ha salido impar, por lo tanto pierdes")
            bet+=1
            jugadas_malas+=str(f"{random_number} ")
            print(f"[+] Te quedas en {money}€")
        else:
          print("[+] Ha salido impar por lo tanto ganas")
          reward=(bet * 2)
          print(f"[+] Has ganado {reward}€")
          money=(money+reward)
          if (money > max_money):
            max_money=money
          print(f"[+] Ahora tienes {money}€")
          if (bet >=11):
            bet-=1
          else:
            bet=10
    else:
      print("[+] Te has quedado sin dinero cabrón")
      break
  print(f"[+] Ha habido un total de {play_counter} jugadas.")
  print(f"[+] A continuación se van a representar los números que no te favorecián: {jugadas_malas}]")
  print(f"[+] El máximo de dinero que has logrado tener es de {max_money}€")

if (initial_money>0) & (technique=="martingala"):
  martingala()
elif (initial_money>0) & (technique=="inverseLabrouchere"):
  inverseLabrouchere()
elif (initial_money>0) & (technique=="fibonacci"):
  fibonacci()
elif (initial_money>0) & (technique=="D_Alembert"):
  D_Alembert()
else:
  helpPanel()