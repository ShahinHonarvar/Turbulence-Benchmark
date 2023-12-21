import re
def insert_after_character(s):
    return re.sub(r'o(?!a)', 'o a', s)
