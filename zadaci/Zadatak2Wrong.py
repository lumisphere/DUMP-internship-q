# Unos broja redaka i stupaca
n = int(input("Unesite broj redaka: "))
m = int(input("Unesite broj stupaca: "))

# Inicijalizacija matrice
matrix = []

# Unos elemenata matrice
print("Unesite elemente matrice:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Izračun sume
result = 0

for i in range(n):
    for j in range(m):
        if (i + 1) % 2 == 1 and (j + 1) % 2 == 1:  # Neparna mjesta
            result -= matrix[i][j]
        elif (i + 1) % 2 == 0 and (j + 1) % 2 == 0:  # Parna mjesta
            result += matrix[i][j]

# Ispis rezultata
print(f"Rezultat: {result}")

input("Pritisnite Enter za izlaz...")