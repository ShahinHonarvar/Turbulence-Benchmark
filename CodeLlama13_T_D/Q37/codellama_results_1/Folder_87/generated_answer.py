
def filter_chars(string):
    filtered = ""
    for char in string:
        if 18 <= ord(char) <= 81 and "W" <= char <= "[":
            continue
        else:
            filtered += char
    return filtered
