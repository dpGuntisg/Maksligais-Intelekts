import re
import nltk


raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"


clean_text = re.sub(r"@\w+", "", raw_text)  
clean_text = re.sub(r"http\S+", "", clean_text)  
clean_text = re.sub(r"[^\w\s]", "", clean_text)  
clean_text = clean_text.lower()  

print(f"Tīrais teksts: {clean_text.strip()}")
