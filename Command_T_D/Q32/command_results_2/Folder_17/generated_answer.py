import re
def insert_after_character(s):
    return re.sub(r'Q([^I])', r'Q\1I', s)
