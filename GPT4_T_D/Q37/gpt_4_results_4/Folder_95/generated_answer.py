
def filter_chars(text):
    chars_to_remove = set(c for i, c in enumerate(text)
                          if 35 <= i <= 40 and ')' <= c <= 'l')
    return ''.join(c for c in text if c not in chars_to_remove)
