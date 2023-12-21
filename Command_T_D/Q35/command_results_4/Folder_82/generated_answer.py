import re
def remove_repeat_chars(text):
    return re.sub(r'(?!<\d){}(?!>200)([a-z])\1(?!<\d)', r'\1', text, flags=re.I)
