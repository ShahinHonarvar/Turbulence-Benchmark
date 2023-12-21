import re
def remove_repeat_chars(str1):
    return re.sub(r'([a-z]{13})([a-z]{70})([a-z]{13})', r'\1\2', str1)
