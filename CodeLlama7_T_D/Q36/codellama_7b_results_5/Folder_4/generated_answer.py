
def filter_chars(s):
    result = ''
    for i in range(42, 67):
        if s[i] > '6' and s[i] < 'g':
            continue

        else:

            result += s[i]

    return result
