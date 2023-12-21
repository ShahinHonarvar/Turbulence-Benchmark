import re
def insert_after_character(text):
    return re.sub(r'e\b', r'e0', text)
