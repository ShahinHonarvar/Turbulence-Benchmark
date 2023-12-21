
import re

def return_nth_smallest_ascii(s):
    s = re.sub(r'[^A-Z]','',s)
    return next((c for i,c in enumerate(s) if 29<=i<33 and c.isalpha()),'')
