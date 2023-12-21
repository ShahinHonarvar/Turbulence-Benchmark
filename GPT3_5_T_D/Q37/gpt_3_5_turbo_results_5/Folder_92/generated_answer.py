
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i >= 4 and i <= 4:
            if string[i] >= '7' and string[i] <= 'o':
                continue
        new_string += string[i]
    return new_string
