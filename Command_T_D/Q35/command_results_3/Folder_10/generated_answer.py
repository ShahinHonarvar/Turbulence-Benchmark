import re
def remove_repeat_chars(str):
    return re.sub(r'((?:[a-z])\1+)', r'\1', str[36:-54])
