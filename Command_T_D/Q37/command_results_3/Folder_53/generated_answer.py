import re
def filter_chars(s):
    return re.sub(r'[^*j](?=.*[A-Z])', '', s)
