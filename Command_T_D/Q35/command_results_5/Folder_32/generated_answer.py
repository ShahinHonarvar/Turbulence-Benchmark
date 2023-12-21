import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=86)|(?<=90)).+(?=86|90)', '', s)
