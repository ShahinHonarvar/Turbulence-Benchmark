import re
def filter_chars(str1):
    str1 = re.sub(r'(?<=.)(r)(?<=.)(t)', '', str1)
    return str1
