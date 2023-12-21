
def filter_chars(string):
    filtered = ""
    for i in range(len(string)):
        if (i < 11 or i > 32) and string[i].isalpha():
            filtered += string[i]
    return filtered
