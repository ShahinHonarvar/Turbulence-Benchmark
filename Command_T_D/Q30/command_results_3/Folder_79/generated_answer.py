import re
def insert_before_character(text):
    return re.sub(r'(?<=E)E', 'EE', text)
