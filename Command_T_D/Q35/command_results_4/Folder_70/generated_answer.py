import re
def remove_repeat_chars(s):
    return re.sub(r'(?<=43).*(?<=70).*(?=43).*(?=70)', '', s)
