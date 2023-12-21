import re
def remove_repeat_chars(str1):
    return re.sub(r'((?<=\d)C)(?=\d)', '', str1)
