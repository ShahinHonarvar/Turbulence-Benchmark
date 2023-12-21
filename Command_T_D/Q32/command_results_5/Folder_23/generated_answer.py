import re
def insert_after_character(text):
    return re.sub(r'b([^by]*)(?=\by)', r'b\1y', text)
