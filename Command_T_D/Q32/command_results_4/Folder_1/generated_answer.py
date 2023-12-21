import re
def insert_after_character(string):
    return re.sub(r'U(?!T)', r'UT', string)
