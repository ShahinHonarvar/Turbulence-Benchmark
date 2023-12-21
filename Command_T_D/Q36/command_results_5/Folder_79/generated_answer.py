 
import re
def filter_chars(s):
    return re.sub(r'(?<=!)([A-Z]{{11,46}})', '', s)
