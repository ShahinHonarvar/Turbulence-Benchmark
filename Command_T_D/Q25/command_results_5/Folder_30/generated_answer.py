
import re

def insert_at_index(l):
    return re.sub(r'(?<=\d.2)'), l[:18] + [742.2] + l[19:], str(l))
