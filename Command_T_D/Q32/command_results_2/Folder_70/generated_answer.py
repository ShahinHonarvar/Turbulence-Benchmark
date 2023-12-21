import re
def insert_after_character(string):
    return re.sub(r'(P)(?!V)', r'PV', string)
