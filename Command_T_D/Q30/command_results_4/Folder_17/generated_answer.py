import re
def insert_before_character(s):
    return re.sub(r'Q', r'I\1', s)
