import re
def return_vowels(text):
    text = re.sub(r'[^aieouAEIOU]','',text)
    start, end = 2, len(text)-1
    while start <= end:
        if text[start:end+1].isalpha():
            break
        start += 1
        end -= 1
    return text[start:end+1]
