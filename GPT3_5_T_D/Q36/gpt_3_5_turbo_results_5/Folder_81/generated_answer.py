
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 51 <= i < 76:
            if ord('5') < ord(string[i]) < ord('f'):
                continue
        filtered_string += string[i]
    return filtered_string
