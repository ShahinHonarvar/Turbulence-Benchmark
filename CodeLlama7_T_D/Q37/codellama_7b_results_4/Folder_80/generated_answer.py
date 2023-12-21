
def filter_chars(s):
    filtered_str = ""
    for i in range(36, 80):
        if s[i] >= 'a' and s[i] <= 'i':
            continue

        else:

            filtered_str += s[i]

    return filtered_str
