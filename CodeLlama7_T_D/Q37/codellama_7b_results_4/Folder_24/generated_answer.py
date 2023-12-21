
def filter_chars(s):
    filtered_str = ''
    for i in range(36, 80):
        char = s[i]
        if char >= '2' and char <= 's':
            continue

        else:

            filtered_str += char

    return filtered_str
