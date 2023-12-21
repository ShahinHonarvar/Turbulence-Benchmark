
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 71 and i <= 96:
            if string[i] >= '_' and string[i] <= 'o':
                continue
        filtered_string += string[i]
    return filtered_string
