import re
def remove_repeat_chars(s):
    return re.sub(r'(?!^)[a-z]{%d,98}{%d}(?!$)'.format(70, 98), '', s)
