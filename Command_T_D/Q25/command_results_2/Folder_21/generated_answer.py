
import re

def insert_at_index(lst):
    return re.sub(r'(?<=\d)\d\.(?=\d)', r'11.04', lst)
