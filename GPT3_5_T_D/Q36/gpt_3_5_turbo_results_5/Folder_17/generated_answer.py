
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 18 or i >= 95:
            filtered_string += string[i]
        elif ord(string[i]) > ord('K') and ord(string[i]) < ord('a'):
            continue
        else:
            filtered_string += string[i]
    return filtered_string
