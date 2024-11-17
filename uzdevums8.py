import nltk


text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

entities = nltk.ne_chunk(tags)

person_names = []
organizations = []

for subtree in entities:
    if isinstance(subtree, nltk.Tree):  
        label = subtree.label()
        if label == 'PERSON': 
            person_names.append(" ".join(word for word, tag in subtree))
        elif label == 'GPE' or label == 'LOCATION': 
            organizations.append(" ".join(word for word, tag in subtree))

# Izvade
print("Personvārdi:", person_names)
print("Organizācijas:", organizations)
