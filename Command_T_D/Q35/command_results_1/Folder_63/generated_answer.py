import re
def remove_repeat_chars(s):
    return re.sub(r'(?i)(?<=\d{5})(\d{2})\1+', r'\1', s)
