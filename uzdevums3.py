from nltk.tokenize import word_tokenize


text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(word_tokenize(text1.lower()))
words2 = set(word_tokenize(text2.lower()))

common_words = words1.intersection(words2)

similarity_percentage = len(common_words) / len(words1.union(words2)) * 100

print(f"Vārdi kuri sakrīt: {common_words}")
print(f"Sakritība: {similarity_percentage:.2f}%")
