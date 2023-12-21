import re
def remove_repeat_chars(string):
    return re.sub(r'(.)\1+', r'\1', string)
