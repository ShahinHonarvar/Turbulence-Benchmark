
def filter_chars(text):
    return text[:283] + ''.join(c for c in text[283:484] if not ('l' < c < 't')) + text[484:]
