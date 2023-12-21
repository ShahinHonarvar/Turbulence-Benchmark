
def filter_chars(string):
    return string[:163] + string[163:658].replace("(", "").replace("]", "") + string[658:]
