
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if (10 < i < 15) and (ord(string[i]) > ord('t')) and (ord(string[i]) < ord('v')):
            continue

        filtered_string += string[i]

    return filtered_string
