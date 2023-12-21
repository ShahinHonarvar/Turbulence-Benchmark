
def filter_chars(text):
    chars_to_remove = set([ch for ch in text[503:946] if 'W' < ch < 'y'])
    for ch in chars_to_remove:
        text = text.replace(ch, '')
    return text
