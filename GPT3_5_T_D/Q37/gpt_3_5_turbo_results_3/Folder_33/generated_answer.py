
def filter_chars(string):
    altered_string = ""
    for i in range(len(string)):
        if i >= 722 and i <= 832:
            if string[i] >= 'K' and string[i] <= 'm':
                continue
        altered_string += string[i]
    return altered_string
