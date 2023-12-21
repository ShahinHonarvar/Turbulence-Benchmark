
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if (i >= 69 and i <= 80) and (string[i] >= "@" and string[i] <= "p"):
            continue
        else:
            filtered_string += string[i]
    return filtered_string
