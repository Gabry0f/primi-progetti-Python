print("===QUIZ DI STORIA===")

giocare_ancora = "si" or "yes"

while giocare_ancora.lower() == "si" or  giocare_ancora.lower() == "yes":
  print("===INIZIO PARTITA===")
  punti = 0

  print("Prima domanda")
  print("in che anno è cominciata la seconda guerra mondiale?")
  opzione1 = int(input("scrivi la risposta giusta: "))

  if opzione1 == 1939:
    print("hai indovinato!!, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("Seconda domanda")
  print("dove morì Napoleone Bonaparte?")
  opzione2 = input("scrivi la risposta giusta:")

  if opzione2.lower() == "isola di sant elena" or opzione2.lower() == "st helena island":
    print("hai indovinato, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("Terza domanda")
  print("quale nazione, all'età dell'imperialismo dell'ottocento/novecento, conquisto la Libya e la Somalia?")
  opzione3 = input("scrivi la risposta giusta: ")

  if opzione3.lower() == "italia" or opzione3.lower() == "italy":
    print("hai indovinato!!, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("risultato finale\n")
  print(f"hai totalizzato {punti} punti")

  print("Quarta domanda")
  print("in che anno fu scoperta l'America?")
  opzione4 = int(input("scrivi la risposta giusta: "))

  if opzione4 == 1492:
    print("hai indovinato!!, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("Quinta domanda")
  print("quale antica civiltà ha costruito il Colosseo?")
  opzione5 = input("scrivi la risposta giusta: ")

  if opzione5.lower() == "romani" or opzione5.lower() == "romans":
    print("hai indovinato!!, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("Sesta domanda")
  print("in quale nazione moderna si trovano le piramidi di Giza?")
  opzione6 = input("scrivi la risposta giusta: ")

  if opzione6.lower() == "egitto" or opzione6 == "egypt":
    print("hai indovinato!!, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  if punti >= 60:
    print("🏆 Congratulazioni!! hai risposto bene a tutte domande")
  elif punti >= 40:
    print("🥈 Ottimo lavoro, c'eri quasi")
  else:
    print("❌ Mi dispiace riprova")

  giocare_ancora = input("vuoi rifare le domande (rispondi con si o no): ")

print("\ngrazie per aver giocato")
