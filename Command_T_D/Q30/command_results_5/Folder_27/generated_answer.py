import re
def insert_before_character(text):
    return re.sub(r'(?<=N)j', 'j', text)
