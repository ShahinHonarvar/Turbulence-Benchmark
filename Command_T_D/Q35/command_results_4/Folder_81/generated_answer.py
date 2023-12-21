import re
def remove_repeat_chars(str):
    return re.sub(r'(.)\1+', r'\1', str)[20:-200]
