import re
def filter_chars(str):
    return re.sub(r'(?!<\s).(?!<\s).(?!<\s).(?!<\s).(?!<\s).(?!<\s).(?!<\s)', '', str)
