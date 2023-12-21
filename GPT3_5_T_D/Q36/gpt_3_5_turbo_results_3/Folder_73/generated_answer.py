
def filter_chars(string):
    altered_string = ""
    for i in range(len(string)):
        if 66 <= i < 90:
            if '#' < string[i] < 'T':
                continue
        altered_string += string[i]
    return altered_string
