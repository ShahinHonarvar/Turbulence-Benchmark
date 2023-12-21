
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalnum():
            continue

        elif string[i] >= '0' and string[i] <= 'k':
            filtered_string += string[i]

    return filtered_string
