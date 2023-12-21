import re
def insert_after_character(text):
    return re.sub(r'(A)', r'A\na', text)
