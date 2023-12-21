import re
def filter_chars(string):
    return re.sub(r'([%u343-665])', '', string)
