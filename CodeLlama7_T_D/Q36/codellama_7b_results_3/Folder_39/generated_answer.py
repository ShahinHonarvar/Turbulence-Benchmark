
def filter_chars(s):
    filtered_str = ""
    for i in range(43, 59):
        if s[i] > '5' and s[i] < 'C':
            continue

        else:

            filtered_str += s[i]

    return filtered_str
