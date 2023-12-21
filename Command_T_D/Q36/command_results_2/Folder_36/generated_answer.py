import re
def filter_chars(string):
    return re.sub(r'(?!t).*(?!l)', '', string)
