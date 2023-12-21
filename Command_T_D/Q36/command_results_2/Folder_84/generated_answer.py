 
import re
def filter_chars(s):
    return re.sub(r'[\x00-\x7f]{171,636}','',s)
