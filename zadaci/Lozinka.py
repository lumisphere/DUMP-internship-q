import re

def provjeri_lozinku(lozinka, x, y, z, w):
    if len(re.findall(r'[a-z]', lozinka)) < x:
        return False
    if len(re.findall(r'[A-Z]', lozinka)) < y:
        return False
    if len(re.findall(r'[!@#$%^&*()_+\-=\{\}\[\]|\\:;"\'<>,.?/]', lozinka)) < z:
        return False
    if len(re.findall(r'\d', lozinka)) < w:
        return False
    return True

# Unos kriterija
x = int(input("Unesi minimalan broj malih slova: "))
y = int(input("Unesi minimalan broj velikih slova: "))
z = int(input("Unesi minimalan broj posebnih znakova: "))
w = int(input("Unesi minimalan broj brojki: "))

# Unos lozinke
lozinka = input("Unesi lozinku: ")

# Provjera lozinke
if provjeri_lozinku(lozinka, x, y, z, w):
    print("Lozinka zadovoljava zadane uvjete!")
else:
    print("Lozinka ne zadovoljava zadane uvjete.")
