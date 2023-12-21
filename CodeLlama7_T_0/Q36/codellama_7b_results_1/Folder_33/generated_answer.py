
def filter_chars(string):
    filtered_string = ""
    for i in range(299, 418):
        if string[i] > '9' and string[i] < 'P':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
