
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if i < 379 or i > 898:
            result += string[i]
        elif not (ord('M') <= ord(string[i]) <= ord('v')):
            result += string[i]
    return result
