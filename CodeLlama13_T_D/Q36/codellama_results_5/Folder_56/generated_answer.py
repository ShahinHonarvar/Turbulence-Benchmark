
def filter_chars(string):
    filtered_str = ""
    for i in range(len(string)):
        if (31 < ord(string[i]) < 50) and string[i] != "/" and string[i] != "J":
            filtered_str += string[i]
    return filtered_str
