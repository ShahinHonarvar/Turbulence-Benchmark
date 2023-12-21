
def filter_chars(text):
    for char in text[16:85]:
        if 'I' < char < 'M':
            text = text.replace(char, '')
    return text
