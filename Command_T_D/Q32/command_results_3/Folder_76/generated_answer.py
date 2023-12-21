import re
def insert_after_character(text):
    return re.sub(r'F(?!m)', r'F\1m', text)
