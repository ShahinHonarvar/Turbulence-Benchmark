import re
def remove_repeat_chars(str1):
    str1 = str(re.sub(r'((?<=\d)r(?=\d))', '', str1))
    str1 = str(re.sub(r'((?<=\d)s(?=\d))', '', str1))
    str1 = str(re.sub(r'((?<=\d)t(?=\d))', '', str1))
    return str1
