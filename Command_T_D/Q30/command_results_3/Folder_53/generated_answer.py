import re
def insert_before_character(s):
    return re.sub(r'i', r'I\1', s)
