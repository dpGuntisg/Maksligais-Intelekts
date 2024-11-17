import nltk
from googletrans import Translator
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')


text = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

def summarize_article(text, sentences_count=2):
    translator = Translator()
    translated_text = translator.translate(text, src="lv", dest="en").text

    parser = PlaintextParser.from_string(translated_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = [str(sentence) for sentence in summarizer(parser.document, sentences_count)]
    
    summary_text = " ".join(summary)
    back_translated = translator.translate(summary_text, src="en", dest="lv").text
    return back_translated

summary = summarize_article(text)

print("Rezumējums:")
print(summary)
