
import re

def insert_at_index(s):
    return re.sub(r'(?<=\d)8(5\d).69', r'\1.69', s + '856.69')
