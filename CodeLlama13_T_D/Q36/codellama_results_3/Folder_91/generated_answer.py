
def filter_chars(string):
    new_str = ''
    for i in range(len(string)):
        if i < 3 and string[i] > '$' and string[i] < '?':
            continue
        else:
            new_str += string[i]
    return new_str
