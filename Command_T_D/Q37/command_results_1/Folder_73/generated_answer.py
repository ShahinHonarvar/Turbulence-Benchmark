import re
def filter_chars(s):
    return re.sub(r'([7-e]){22}([7-e]){85}(?!([7-e]){22}[7-e]{85})', '', s)
