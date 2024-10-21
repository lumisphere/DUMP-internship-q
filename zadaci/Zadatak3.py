def are_anagrams(str1, str2):
    # Uklanjamo razmake i pretvaramo sve u mala slova
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Ako stringovi nisu iste duljine, nisu anagrami
    if len(str1) != len(str2):
        return False
    
    # Stvaramo rječnike za brojanje znakova
    char_count1 = {}
    char_count2 = {}
    
    # Brojimo znakove u oba stringa
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Uspoređujemo rječnike
    return char_count1 == char_count2

# Glavni dio programa za korisnički unos
if __name__ == "__main__":
    print("Unesite dvije riječi ili fraze za provjeru anagrama:")
    word1 = input("Prva riječ ili fraza: ")
    word2 = input("Druga riječ ili fraza: ")
    
    result = are_anagrams(word1, word2)
    
    if result:
        print(f"'{word1}' i '{word2}' su anagrami.")
    else:
        print(f"'{word1}' i '{word2}' nisu anagrami.")


input("Pritisnite Enter za izlaz...")