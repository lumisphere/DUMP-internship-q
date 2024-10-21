def najduzi_rastuci_podniz(niz):
  """Pronalazi najduži rastući podniz unutar danog niza.

  Args:
    niz: Lista cijelih brojeva.

  Returns:
    Najduži rastući podniz.
  """

  n = len(niz)
  if n == 0:
    return []

  duzine = [1] * n
  prethodnik = [None] * n

  # Pronalazi dužine i prethodnike za sve rastuće podnizove
  for i in range(1, n):
    for j in range(i):
      if niz[i] > niz[j] and duzine[i] < duzine[j] + 1:
        duzine[i] = duzine[j] + 1
        prethodnik[i] = j

  # Pronalazi indeks zadnjeg elementa najdužeg podniza
  maks_indeks = 0
  for i in range(n):
    if duzine[i] > duzine[maks_indeks]:
      maks_indeks = i

  # Rekonstruira najduži podniz
  podniz = []
  i = maks_indeks
  while i is not None:
    podniz.append(niz[i])
    i = prethodnik[i]

  return podniz[::-1]

# Unos podataka
n = int(input("Unos n: "))
niz = list(map(int, input("Unos: ").split()))

# Pronalazi i ispisuje najduži rastući podniz
podniz = najduzi_rastuci_podniz(niz)
print("Izlaz:", *podniz)

input("Pritisnite Enter za izlaz...")