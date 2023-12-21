import re
def remove_repeat_chars(s):
    return re.sub(r"((?<=86).*(?<=99))", lambda m: m.group(1).replace("*",""), s)
