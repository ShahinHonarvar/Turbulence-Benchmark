import re
def filter_chars(str):
    return re.sub(r'(?!<=20)(?<=25)', '', str)
