
def filter_chars(s):
    result = ""
    for i in range(1, len(s)):
        if s[i] > '8' and s[i] < 'm':
            continue

        result += s[i]

    return result
