import os

msg = os.getenv("MY_MESSAGE", "Brak zmiennej!")
print("Wartość zmiennej środowiskowej:", msg)
