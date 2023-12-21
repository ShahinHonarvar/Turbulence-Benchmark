
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha() and (ord(string[i]) >= ord('E') and ord(string[i]) <= ord('~')):
            filtered_string += string[i]
    return filtered_string
