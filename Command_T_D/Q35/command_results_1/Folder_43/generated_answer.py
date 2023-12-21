import re
def remove_repeat_chars(text):
    return re.sub(r'(?!\d){10}(.)\1{17}(?!\d){28}', r'\1', text)
