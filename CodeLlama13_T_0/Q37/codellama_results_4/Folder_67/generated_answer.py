
def filter_chars(string):
    result = ""
    for char in string:
        if char not in "]t":
            result += char
    return result
