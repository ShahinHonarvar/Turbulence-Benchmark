
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i] != "_" and string[i] != "o":
            filtered_string += string[i]
    return filtered_string
