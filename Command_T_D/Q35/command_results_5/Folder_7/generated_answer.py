import re
def remove_repeat_chars(text):
    return re.sub(r'(.)\1+\1*', r'\1', text[375:-26])
