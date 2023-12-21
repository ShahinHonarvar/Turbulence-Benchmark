import re
def filter_chars(string):
    return re.sub(r'[^!}]{170,195}', '', string)
