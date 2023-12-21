
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] >= '8' and string[i] <= 'e':
            continue
        else:
            new_str += string[i]
    return new_str
