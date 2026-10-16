import time

print("=== 📦 AMAZON TECH HUB - GESTIONE LOGISTICA ===")

magazzino = ["smartphone", "computer", "tablet", "cuffie", "scarpe"]

scelta_utente = input("scrivi l'articolo che vuoi comprare: ").lower()

if scelta_utente in magazzino:
  print("🟢 Prodotto disponibile, Preparazione della spedizione in corso...")
  time.sleep(2)
  print("ci vorranno pochi secondi...")
  time.sleep(10)
  print("📦 Prodotto spedito! L'arrivo è tra tre giorni")
else:
  print("❌ Ci dispiace, il prodotto è esaurito o non è presente in magazzino")

