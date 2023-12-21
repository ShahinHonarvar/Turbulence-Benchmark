import re
def filter_chars(s):
    return re.sub(r'([^`~!@#$%^-&*()<>?/]))', '', s, flags=re.DOTALL)
