import re
def remove_repeat_chars(s):
    return re.sub(r'(?i)(?<=.)\1+(?<=.)', '', s, flags=re.I)
