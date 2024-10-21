import re
from collections import Counter

def find_most_common_word(text):
    # Pretvaranje teksta u mala slova
    text = text.lower()
    
    # Uklanjanje interpunkcijskih znakova i brojeva
    words = re.findall(r'\b[a-zčćđšž]+\b', text)
    
    # Brojanje riječi
    word_counts = Counter(words)
    
    # Pronalaženje riječi s najviše ponavljanja
    most_common_word = word_counts.most_common(1)[0]
    
    return most_common_word

# Zadani tekst
text = """Od 2008. godine mladi programeri s FESB-a i učenici splitskog MIOC-a održavali su Škole Osnova Programiranja i išli na razna natjecanja. Uvijek se rado sjećamo svjetskog finala Imagine Cupa natjecanja u Poljskoj. Dok smo se uz pizzu i geek igre družili u računalnim labovima na FESB-u, razmišljali smo je li to sve što možemo ponuditi lokalnoj zajednici. Tada se rodila ideja formalnog osnivanja Udruge, koja je svojim ostvarenjem i početnim radom počela širiti kako vlastite horizonte, tako i one budućih članova."""

# Pronalaženje najčešće riječi
word, count = find_most_common_word(text)

# Ispis rezultata
print(f"Riječ koja se najviše ponavlja je '{word}' s {count} ponavljanja.")
