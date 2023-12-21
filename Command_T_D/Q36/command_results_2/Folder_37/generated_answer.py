import re
def filter_chars(str):
    return re.sub(r'[0-5](?=[/]|$)', '', str)
