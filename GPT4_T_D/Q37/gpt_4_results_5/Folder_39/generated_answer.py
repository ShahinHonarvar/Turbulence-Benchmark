
def filter_chars(text):
    for i in range(52, min(82, len(text))):
        if 'A' <= text[i] <= 'U':
            text = text.replace(text[i], '')
    return text
