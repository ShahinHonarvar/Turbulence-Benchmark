
def filter_chars(text):
    substring = text[15:56]
    to_remove = [char for char in substring if 'W' <= char <= '{']
    for char in to_remove:
        text = text.replace(char, '')
    return text
