import re
def remove_repeat_chars(s):
    return re.sub(r'(?<=86)(?=90)'.join(x*2 for x in set(s)), '', s)
