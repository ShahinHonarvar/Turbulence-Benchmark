import re
def all_pos_ints_exclusive(s):
    return [int(i) for i in re.findall(r'(?<!\d)[0-9][1-9][0-9]'.replace('!', ''), s)]
