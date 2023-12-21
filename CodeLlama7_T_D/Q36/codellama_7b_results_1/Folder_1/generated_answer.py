
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha() and (ord(string[i]) > 69 and ord(string[i]) < 87):
            continue
        else:
            filtered_string += string[i]
    return filtered_string
