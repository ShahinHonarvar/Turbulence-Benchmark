import re
def filter_chars(s):
    return re.sub(r'(?<=.)l(?!t)', '', s, flags=re.I)
