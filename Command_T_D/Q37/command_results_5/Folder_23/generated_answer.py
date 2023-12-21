import re
def filter_chars(s):
    return re.sub(r'[Vv]?(?=([^Vv]51[^Vv]77[^Vv]))', '', s)
