
def filter_chars(text):
    removed_chars = {char for char in text[477:948] if 'b' < char < 'd'}
    result = ''.join(char for char in text if char not in removed_chars)
    return result
