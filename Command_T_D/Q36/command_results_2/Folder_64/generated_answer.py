import re
def filter_chars(s):
    return re.sub(r'(?i)(?<=.)[1-7](?=.)', '', s)
