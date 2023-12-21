import re
def filter_chars(text):
    return re.sub(r'[a-h]([A-e])', r'\1', text)
