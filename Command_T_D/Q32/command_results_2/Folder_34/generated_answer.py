import re
def insert_after_character(string):
    return re.sub(r'(A)','a\1',string)
