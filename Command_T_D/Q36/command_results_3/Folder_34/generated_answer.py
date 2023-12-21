import re
def filter_chars(str):
    return re.sub(r'(?!<10)>(?!79)<[?a-m]', '', str)
