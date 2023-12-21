import re
def filter_chars(string):
    return re.sub(r'[>._~]{%38,%81}', '', string)
