from langdetect import detect

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

print("Tekstu valodas noteikšana:")
for i, text in enumerate(texts, start=1):
    try:
        lang_code = detect(text)
        print(f"Teksts {i}: '{text}' - Valoda: {lang_code}")
    except Exception as e:
        print(f"Teksts {i}: '{text}' - Error: {e}")
