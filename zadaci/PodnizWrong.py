def najduzi_rastuci_podniz(niz):
    n = len(niz)
    if n == 0:
        return []

    # Inicijalizacija
    LIS = [1] * n
    prev = [-1] * n

    # Računanje LIS
    for i in range(1, n):
        for j in range(i):
            if niz[i] > niz[j] and LIS[i] < LIS[j] + 1:
                LIS[i] = LIS[j] + 1
                prev[i] = j

    # Pronalaženje maksimalne dužine i početka rekonstrukcije
    max_index = LIS.index(max(LIS))

    # Rekonstrukcija podniza
    rezultat = []
    while max_index != -1:
        rezultat.append(niz[max_index])
        max_index = prev[max_index]
    
    return rezultat[::-1]  # Obrnuti redoslijed jer smo gradili od kraja

# Ulaz
n = int(input("Unos n: "))
niz = list(map(int, input("Unos: ").strip().split()))

# Poziv funkcije i ispis
print("Izlaz:", " ".join(map(str, najduzi_rastuci_podniz(niz))))
