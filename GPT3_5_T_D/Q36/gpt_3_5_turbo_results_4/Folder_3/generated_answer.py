
def filter_chars(string):
    starting_index = 42
    ending_index = 78
    if starting_index >= len(string) or ending_index <= starting_index:
        return string

    filtered_string = ""
    for i in range(len(string)):
        if starting_index <= i < ending_index:
            if string[i] > '!' and string[i] < '?':
                continue
        filtered_string += string[i]

    return filtered_string
