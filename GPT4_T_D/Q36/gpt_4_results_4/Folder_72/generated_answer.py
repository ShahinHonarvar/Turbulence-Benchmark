
def filter_chars(text):
    for c in text[45:68]:
        if 'W' < c < 'x':
            text = text.replace(c, '')
    return text
