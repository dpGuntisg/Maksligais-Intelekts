import nltk
import string
from collections import Counter

# Teksts
text = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas.
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.
"""

# Teksta apstrāde
# 1. Noņemt pieturzīmes
text_clean = text.translate(str.maketrans('', '', string.punctuation))

# 2. Konvertēt uz maziem burtiem
text_clean = text_clean.lower()

# 3. Tokenizēt vārdus (vienkārša atdalīšana)
tokens = text_clean.split()

# 4. Saskaitīt biežumus
freq_dist = Counter(tokens)

# 5. Izvadīt rezultātus
print("Vārdu biežums tekstā:")
for word, count in freq_dist.items():
    print(f"{word}: {count}")

