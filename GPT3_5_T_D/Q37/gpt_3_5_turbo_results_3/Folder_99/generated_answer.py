
def filter_chars(string):
    altered_string = ""
    for i in range(len(string)):
        if i >= 373 and i <= 901 and string[i] >= 'T' and string[i] <= 'h':
            altered_string += string[i].replace(string[i], '')
        else:
            altered_string += string[i]
    return altered_string
