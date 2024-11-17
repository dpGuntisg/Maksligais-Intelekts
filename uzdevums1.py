import nltk
import string
from collections import Counter


text = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas.
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.
"""

text_clean = text.translate(str.maketrans('', '', string.punctuation))

text_clean = text_clean.lower()

tokens = text_clean.split()

freq_dist = Counter(tokens)

print("Vārdu biežums tekstā:")
for word, count in freq_dist.items():
    print(f"{word}: {count}")

