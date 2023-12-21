import re
def remove_repeat_chars(s):
    return re.sub(r'(?i)(?=([A-Z]))\1+', '', s)
