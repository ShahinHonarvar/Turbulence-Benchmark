
def filter_chars(string):
    new_string = ''
    for i in range(344, 874):
        if string[i].isalpha():
            new_string += string[i]
    return new_string
