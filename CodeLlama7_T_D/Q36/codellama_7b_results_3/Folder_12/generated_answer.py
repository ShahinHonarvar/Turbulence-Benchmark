
def filter_chars(s):
    filtered = ""
    for i in range(len(s)):
        if s[i] > 'm' and s[i] < 'w':
            continue

        else:

            filtered += s[i]

    return filtered
