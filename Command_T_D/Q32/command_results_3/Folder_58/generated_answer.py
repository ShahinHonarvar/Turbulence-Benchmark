import re
def insert_after_character(s):
    return re.sub(r'F(.)', r'Fo\1', s)
