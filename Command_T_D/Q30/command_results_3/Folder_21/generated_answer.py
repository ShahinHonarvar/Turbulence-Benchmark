import re
def insert_before_character(string):
    return re.sub(r'(.)\sK', r'\1K', string)
