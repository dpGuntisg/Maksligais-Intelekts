from googletrans import Translator

texts = ["Labdien! Kā jums klājas?", "Es šodien lasīju interesantu grāmatu."]

translator = Translator()

for text in texts:
    translation = translator.translate(text, src='lv', dest='en')
    print(f"Ievades teksts: {text}")
    print(f"Tulkots teksts: {translation.text}")
