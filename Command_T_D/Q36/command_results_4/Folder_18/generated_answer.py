import re
def filter_chars(s):
    return re.sub(r'(?!,)[\d\w]+(?!c)', '', s)
