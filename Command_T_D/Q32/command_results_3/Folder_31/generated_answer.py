import re
def insert_after_character(s):
    return re.sub(r'B([^N]*?)', r'BN\1', s)
