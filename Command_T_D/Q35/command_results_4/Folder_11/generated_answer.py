import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=.)[A-PZ]52)', '', s)
