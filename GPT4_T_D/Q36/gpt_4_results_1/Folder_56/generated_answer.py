
def filter_chars(text):
    chars_to_remove = [char for char in text[32:50] if '/' < char < 'J']
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text
