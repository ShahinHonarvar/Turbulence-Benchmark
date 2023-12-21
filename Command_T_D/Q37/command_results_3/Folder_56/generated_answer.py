import re
def filter_chars(text):
    return re.sub(r'(?i)[A-Z][^a]*', '', text)
