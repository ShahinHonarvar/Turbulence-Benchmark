
def filter_chars(text):
    return ''.join(char for i, char in enumerate(text) if not (19 <= i <= 90 and 'F' <= char <= 'h'))
