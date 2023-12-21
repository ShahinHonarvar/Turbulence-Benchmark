import re
def filter_chars(s):
    return re.sub(r'(?<=.)(?!-)[0-7](?!L)', '', s)
