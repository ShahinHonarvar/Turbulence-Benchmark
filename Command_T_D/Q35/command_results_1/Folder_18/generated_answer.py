import re
def remove_repeat_chars(text):
    return re.sub(r'([A-Z])\1+', r'\1', text)
