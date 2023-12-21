import re
def remove_repeat_chars(s):
    return re.sub(r'((?<= )|(?<=\A))([a-z]{5})((?=\ )|(?=\A))', r'\1', s)
