
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i >= 21 and i <= 43:
            if string[i] >= '+' and string[i] <= '8':
                continue
        new_string += string[i]
    return new_string
