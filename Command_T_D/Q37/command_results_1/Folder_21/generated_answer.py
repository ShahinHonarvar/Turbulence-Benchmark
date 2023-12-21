import re
def filter_chars(text):
    return re.sub(r'[qhq]([a-z])', r'\1', text)
