import re
def remove_repeat_chars(text):
    return re.sub(r'(.)\1+\d+|\d+\1+\d+|\d+\1+', '', text)
