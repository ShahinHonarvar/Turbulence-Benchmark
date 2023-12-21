import re
def insert_after_character(text):
    return re.sub(r'(.*?)Y(.*?)', r'\1Y4\2', text)
