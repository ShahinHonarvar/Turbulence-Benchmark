
def filter_chars(string):
    filtered = ""
    for i in range(114, 639+1):
        if string[i].isalnum():
            filtered += string[i]
    return filtered
