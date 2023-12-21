
def filter_chars(text):
    chars_to_remove = [c for c in text[36:80] if '2' <= c <= 's']
    filtered_text = ''.join(c for c in text if c not in chars_to_remove)
    return filtered_text
