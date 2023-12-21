
def filter_chars(string):
    result = ""
    for i in range(3, len(string)):
        if string[i] > '*' and string[i] < 'E':
            continue

        else:

            result += string[i]

    return result
