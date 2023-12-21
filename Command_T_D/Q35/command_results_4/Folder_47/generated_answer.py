import re
def remove_repeat_chars(text):
    return re.sub(r'((?<=\d)[a-z])\1+(?=\d)', '', text)
