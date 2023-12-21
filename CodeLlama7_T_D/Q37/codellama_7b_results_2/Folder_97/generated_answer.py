
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha() and ord(string[i]) >= 227 and ord(string[i]) <= 235:
            continue

        else:

            filtered_string += string[i]

    return filtered_string
