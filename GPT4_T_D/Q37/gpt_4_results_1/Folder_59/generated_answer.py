
def filter_chars(s):
    filter_chars = [char for char in s[2:4] if '5' <= char <= '_']
    result = ""
    for char in s:
        if char not in filter_chars:
             result += char
    return result
