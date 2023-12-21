import re
def insert_after_character(s):
    return re.sub(r'I(?!I)', r'I\1I', s)
