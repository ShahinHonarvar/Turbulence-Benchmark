import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=450)\1+)(?<=905)', '', s)
