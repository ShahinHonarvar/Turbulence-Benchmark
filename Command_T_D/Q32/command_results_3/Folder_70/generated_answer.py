import re
def insert_after_character(s):
    return re.sub(r'P([^V])', r'PV\1', s)
