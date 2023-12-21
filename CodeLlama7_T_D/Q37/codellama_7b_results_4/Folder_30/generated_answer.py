
def filter_chars(s):
    filtered_str = ""
    for i in range(41, 65):
        if s[i] >= 'K' and s[i] <= ']':
            continue

        else:

            filtered_str += s[i]

    return filtered_str
