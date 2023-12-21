import re
def remove_repeat_chars(str1):
    return re.sub(r'((?<=\d)D|(?!\d\1)D)', '', str1[44:-78])
