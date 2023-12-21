import re
def insert_after_character(s):
    return re.sub(r"(.*)\.", r"\1P.", s)
