
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if 23 <= i < 83: 
            if 'f' < string[i] < 'o':
                continue
        new_string += string[i]
    return new_string
