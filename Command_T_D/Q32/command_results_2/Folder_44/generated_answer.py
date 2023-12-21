import re
def insert_after_character(s):
    return re.sub(r"g(?!M)", "Mg", s)
