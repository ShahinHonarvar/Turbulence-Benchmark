import re
def remove_repeat_chars(str):
    str = re.sub(r'((?<=50)\1+(?=92))', '', str)
    return str
