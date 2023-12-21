import re
def insert_before_character(string):
    return re.sub(r'(?<=N)j', '', string)
