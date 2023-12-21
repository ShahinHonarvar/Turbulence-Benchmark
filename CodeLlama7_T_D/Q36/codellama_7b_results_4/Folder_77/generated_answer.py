
def filter_chars(string):
    filtered = ""
    for i in range(221, 419):
        if string[i] > '-' and string[i] < 'v':
            continue

        else:

            filtered += string[i]

    return filtered
