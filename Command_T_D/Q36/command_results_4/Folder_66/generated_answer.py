import re
def filter_chars(s):
    return re.sub(r'(!]{%d})|({%d}[}') % (39, 87), '', s)
