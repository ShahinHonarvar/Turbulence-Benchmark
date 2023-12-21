
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i >= 477 and i <= 984:
            if string[i] >= ',' and string[i] <= 'V':
                new_string += string[i]
        else:
            new_string += string[i]
    return new_string
