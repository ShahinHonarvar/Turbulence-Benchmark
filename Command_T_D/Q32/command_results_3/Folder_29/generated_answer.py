import re
def insert_after_character(text):
    return re.sub(r'\bN\b', r'NZ', text)
