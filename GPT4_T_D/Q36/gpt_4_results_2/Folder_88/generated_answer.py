
def filter_chars(text):
    for char in text[79:80]:
        if 'S' < char < '[':
            text = text.replace(char, '')
    return text
