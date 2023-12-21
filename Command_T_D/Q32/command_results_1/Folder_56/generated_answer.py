import re
def insert_after_character(s):
    return re.sub(r'I(?!i)', r'I\1i', s)
