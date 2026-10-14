print("===QUIZ DI STORIA===")
print("Fai la somma di tutti i punti per sapere il tuo risultato\n")

giocare_ancora = "si"

while giocare_ancora == "si":
  print("===INIZIO PARTITA===")
  punti = 0

  print("Prima domanda")
  print("in che anno è cominciata la seconda guerra mondiale?")
  opzione1 = int(input("scrivi la risposta giusta"))

  if opzione1 == 1939:
    print("hai indovinato!!, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("Seconda domanda")
  print("dove morì Napoleone Bonaparte?")
  opzione2 = input("scrivi la risposta giusta (se la risposta contiene più parole, si scrivono tutte attaccate)")

  if opzione2 == "IsoladiSantElena" or opzione2 == "St Helena Island":
    print("hai indovinato, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("Terza domanda")
  print("quale nazione, all'età dell'imperialismo dell'ottocento/novecento, conquisto la Libya e la Somalia")
  opzione3 = input("scrivi la risposta giusta")

  if opzione3 == "Italia" or opzione3 == "Italy":
    print("hai indovinato!!, (+10 punti)\n")
    punti = punti + 10
  else:
    print("hai sbagliato, (0 punti)\n")

  print("risultato finale\n")
  print(f"hai totalizzato {punti} punti")

  if punti >= 30:
    print("congratulazioni hai risposto bene alle domande")
  else:
    print("mi dispiace riprova")

  giocare_ancora = input("vuoi rifare le domande (rispondi con si o no): ")

print("\ngrazie per aver giocato")
