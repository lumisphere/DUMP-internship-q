def izracunaj_sumu(matrica):
  """Izračunava sumu brojeva u matrici prema zadanim pravilima.

  Args:
    matrica: Lista lista, predstavlja matricu brojeva.

  Returns:
    Suma brojeva u matrici.
  """

  suma = 0
  redova = len(matrica)
  stupaca = len(matrica[0])

  for i in range(redova):
    for j in range(stupaca):
      if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
        suma += matrica[i][j]
      else:
        suma -= matrica[i][j]

  return suma

# Unos podataka
n = int(input("Unos n: "))
m = int(input("Unos m: "))

matrica = []
for i in range(n):
  red = list(map(int, input().split()))
  matrica.append(red)

# Izračunavanje i ispis rezultata
rezultat = izracunaj_sumu(matrica)
print("Rezultat:", rezultat)

input("Pritisnite Enter za izlaz...")