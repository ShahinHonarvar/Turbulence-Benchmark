
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if (i < 170 or i > 195) and string[i] != '!' and string[i] != '}':
            filtered_string += string[i]
    return filtered_string
