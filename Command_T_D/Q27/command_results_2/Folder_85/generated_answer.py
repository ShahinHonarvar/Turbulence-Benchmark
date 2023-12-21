
import re

def insert_after_index(lst):
    return [int(i) for i in re.findall(r'(\d+)', lst[0])] + [304.62] + lst[1:]
