import random 

print("=== 🔐 GENERATORE DI PASSWORD SICURE ===")
print("Rispondi a queste domande e l'AI creerà una password impossibile da hackerare!\n")

# --- PASSO 1: RACCOLTA DATI ---
parola_preferita = input("Inserisci la tua parola preferita: ")
animale = input("Qual è il tuo animale preferito? ")
anno_nascita = int(input("In che anno sei nato? "))

# --- PASSO 2: GENERAZIONE DEL NUMERO CASUALE ---
numero_casuale = random.randint(100, 999)

# --- PASSO 3: UNIAMO TUTTO CON LA F-STRING ---
password = f"{parola_preferita}{animale}{anno_nascita}{numero_casuale}!"

# --- PASSO 4: MOSTRIAMO LA PASSWORD SULLO SCHERMO ---
print("\n🔒 Ecco la tua nuova password super sicura:")
print(password)
