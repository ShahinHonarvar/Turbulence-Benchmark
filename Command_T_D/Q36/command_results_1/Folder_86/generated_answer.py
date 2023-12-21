 
import re
def filter_chars(s):
    return re.sub(r'(?<=\A)X(\d)(?<=\D)', '', s)
