
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if (25 <= i <= 97) and (ord(string[i]) >= ord('m') and ord(string[i]) <= ord('w')):
            continue

        else:

            filtered_string += string[i]

    return filtered_string
