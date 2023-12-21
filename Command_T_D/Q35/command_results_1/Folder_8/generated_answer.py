import re
def remove_repeat_chars(s):
    return re.sub(r'(?!^).*(?<=.45).*(?=.48).*(?!\1).*$', '', s)
