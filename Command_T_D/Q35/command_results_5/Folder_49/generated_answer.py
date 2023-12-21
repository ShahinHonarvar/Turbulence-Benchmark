import re
def remove_repeat_chars(str):
    return re.sub(r'((?<=90)\1+(?<=200))', '', str)
