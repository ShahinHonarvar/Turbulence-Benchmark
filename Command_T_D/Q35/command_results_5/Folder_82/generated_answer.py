import re
def remove_repeat_chars(text):
    return re.sub(r'(\w{30,200})\1', r'\1', text)
