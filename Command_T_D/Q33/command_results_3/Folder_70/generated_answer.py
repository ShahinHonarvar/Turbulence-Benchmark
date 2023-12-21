import re
def return_vowels(text):
    text = re.sub(r'[^A-z]', '', text)
    text = text[171:-1]
    text = text[:text.index('k')]
    return [c for c in text if c.lower() in 'aeiou']
