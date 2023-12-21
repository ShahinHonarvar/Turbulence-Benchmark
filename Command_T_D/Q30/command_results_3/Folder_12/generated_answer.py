import re
def insert_before_character(string):
    return re.sub(r'(?<=I)I', ' I', string)
