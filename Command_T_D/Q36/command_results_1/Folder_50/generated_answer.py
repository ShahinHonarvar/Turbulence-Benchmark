import re
def filter_chars(str):
    return re.sub(r'(?!%#)(?<=\D)[\u0062-\u007e]', '', str)
