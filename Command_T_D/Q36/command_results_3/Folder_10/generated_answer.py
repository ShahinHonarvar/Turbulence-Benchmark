import re
def filter_chars(s):
    return re.sub(r'(?i)(?<=!)([A-Z])([A-Z]![A-Z]![A-Z]![A-Z])', '', s)
