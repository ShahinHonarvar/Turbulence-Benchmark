 
import re
def filter_chars(s):
    return re.sub(r'[^A-Ga-g][^D-f][^g-i][^j-n]', '', s)
