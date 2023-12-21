import re
def insert_before_character(s):
    return re.sub(r'(M)','f\1',s)
