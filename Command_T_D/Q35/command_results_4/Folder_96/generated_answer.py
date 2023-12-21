import re
def remove_repeat_chars(s):
    for i in range(60, 200):
        if s[i] in s[:i]:
            s = re.sub(r"%s+".format(s[i]), s[i], s)
    return s
