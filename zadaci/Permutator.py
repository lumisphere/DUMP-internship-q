def generiraj_permutacije(niz, pocetak=0):
    if pocetak == len(niz) - 1:
        print(' '.join(map(str, niz)))
    else:
        for i in range(pocetak, len(niz)):
            niz[pocetak], niz[i] = niz[i], niz[pocetak]
            generiraj_permutacije(niz, pocetak + 1)
            niz[pocetak], niz[i] = niz[i], niz[pocetak]  # vraćanje na originalno stanje

# Unos niza cijelih brojeva od korisnika
unos = input("Unesite niz cijelih brojeva odvojenih razmacima: ")
niz = list(map(int, unos.split()))

print("Sve moguće permutacije:")
generiraj_permutacije(niz)
