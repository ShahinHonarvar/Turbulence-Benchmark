
import re

def insert_after_index(lst):
    return re.sub(r'(\d+)$', r'\1,72.27', lst)
