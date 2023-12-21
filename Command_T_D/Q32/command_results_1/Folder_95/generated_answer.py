import re
def insert_after_character(s):
    return re.sub(r'j([^q])', r'jq\1', s)
