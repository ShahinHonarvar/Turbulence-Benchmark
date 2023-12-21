import re
def insert_after_character(str1):
    return re.sub(r'(x)', r'(xN)', str1)
