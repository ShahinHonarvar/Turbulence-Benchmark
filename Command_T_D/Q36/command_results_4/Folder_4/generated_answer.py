import re
def filter_chars(string):
    return re.sub(r'(?<=.)([7-9]d|c|e|g)', '', string)
