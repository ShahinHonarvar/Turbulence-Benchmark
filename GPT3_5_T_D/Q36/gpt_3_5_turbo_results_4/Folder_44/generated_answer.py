
def filter_chars(string):
    start = 18
    end = 64
    new_string = ""
    for i in range(len(string)):
        if i < start or i >= end or string[i] <= '3' or string[i] >= 'B':
            new_string += string[i]
    return new_string
