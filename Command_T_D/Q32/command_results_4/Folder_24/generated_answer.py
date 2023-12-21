import re
def insert_after_character(s):
    return re.sub(r'0(?!4)', r'04', s)
