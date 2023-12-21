import re
def remove_repeat_chars(s):
    return re.sub(r'(?!<\d\d)(?<=\d\d).*?(?=\d\d\1)', '', s)
