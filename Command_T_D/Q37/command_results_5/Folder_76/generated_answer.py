import re
def filter_chars(s):
    return re.sub(r'(?<=379)[Mv](?=898)', '', s)
