import re
def remove_repeat_chars(s):
    return re.sub(r'([a-z]){20}([a-z]){35}(?!\1)', r'\2', s)
