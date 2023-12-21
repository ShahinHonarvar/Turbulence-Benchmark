import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1+([^a-z]{50,92})', r'\1\2', s)
