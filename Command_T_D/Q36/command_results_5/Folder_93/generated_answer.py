import re
def filter_chars(str1):
    return re.sub(r'(?i)(?<=&)[\u0052-\u0088]', '', str1)
