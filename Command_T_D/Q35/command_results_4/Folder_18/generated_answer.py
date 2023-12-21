import re
def remove_repeat_chars(s):
    return re.sub(r'(?i)(?<=56)(\D+)(?=90)', '', s)
