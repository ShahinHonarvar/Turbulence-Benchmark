
def filter_chars(text):
    if len(text) < 640:
        removed_chars = set(text[114:])
    else:
        removed_chars = set(text[114:640])
    removed_chars = {ch for ch in removed_chars if '!' <= ch <= 'x'}
    return ''.join(ch for ch in text if ch not in removed_chars)
