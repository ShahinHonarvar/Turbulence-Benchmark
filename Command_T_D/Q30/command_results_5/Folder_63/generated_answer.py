import re
def insert_before_character(text):
    return re.sub(r'(?<=5)R', 'R', text)
