import re
def filter_chars(s):
    return re.sub(r'([;]\d){2}(r)', '', s)
