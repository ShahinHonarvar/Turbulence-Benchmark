import re
def insert_before_character(text):
    return re.sub(r'(?!4)Y', '4Y', text)
