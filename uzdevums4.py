import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator


sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

translator = Translator()

for sentence in sentences:
    translated_sentence = translator.translate(sentence, src='lv', dest='en').text
    print(f"Tulkots teikums: '{translated_sentence}'")

    score = analyzer.polarity_scores(translated_sentence)
    if score['compound'] > 0.05:
        sentiment = "Pozitīvs"
    elif score['compound'] < -0.05:
        sentiment = "Negatīvs"
    else:
        sentiment = "Neitrāls"
    print(f"Teikums: '{sentence}' - Noskaņojums: {sentiment}")
