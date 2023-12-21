import re
def insert_after_character(text):
    return re.sub(r's\w+', r'sw\w+', text)
