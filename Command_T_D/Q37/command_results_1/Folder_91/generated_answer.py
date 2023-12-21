 
import re
def filter_chars(s):
    return re.sub(r'((?<=A)[B-H](?=C))', '', s)
