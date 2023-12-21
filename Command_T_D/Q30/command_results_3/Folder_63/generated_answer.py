import re
def insert_before_character(string):
    return re.sub(r'(?<=5)R', '5', string)
