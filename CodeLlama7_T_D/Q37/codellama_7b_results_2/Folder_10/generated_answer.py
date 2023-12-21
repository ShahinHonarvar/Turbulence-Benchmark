
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha() and ord(string[i]) >= 63 and ord(string[i]) <= 84:
            if string[i] == "E" or string[i] == "~":
                filtered_string += string[i]
    return filtered_string
