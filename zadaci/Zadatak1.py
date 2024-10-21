def perform_operation(op, numbers):
    if op == 'X':
        return numbers[0] + numbers[1]
    elif op == 'Y':
        return numbers[0] * numbers[1]
    elif op == 'Z':
        return (numbers[0] + numbers[1]) * numbers[2]
    elif op == 'W':
        return (numbers[0] + numbers[2]) ** (numbers[1] + numbers[3])
    else:
        return "Nepoznata operacija"

# Unos podataka
operation = input("Unesite tip operacije (X, Y, Z ili W): ")
numbers = list(map(int, input("Unesite brojeve odvojene razmakom: ").split()))

# Izračun i ispis rezultata
result = perform_operation(operation, numbers)
print(f"Rezultat: {result}")

# Dodajte ovu liniju na kraj skripte
input("Pritisnite Enter za izlaz...")