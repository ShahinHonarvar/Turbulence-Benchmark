import re
def insert_before_character(s):
    return re.sub(r"((?<= )K) (.*)"), r"K \1", s)
