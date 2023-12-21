
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha() and (string[i].lower() >= 'j' or string[i].lower() <= 'q') and i > 87 and i < 91:
            continue
        else:
            filtered_string += string[i]
    return filtered_string
