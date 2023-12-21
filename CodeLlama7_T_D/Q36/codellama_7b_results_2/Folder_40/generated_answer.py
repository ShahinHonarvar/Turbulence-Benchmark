
def filter_chars(string):
    new_string = ""
    for i in range(1, len(string)):
        if string[i] > '-' and string[i] < 'L':
            continue

        else:

            new_string += string[i]

    return new_string
