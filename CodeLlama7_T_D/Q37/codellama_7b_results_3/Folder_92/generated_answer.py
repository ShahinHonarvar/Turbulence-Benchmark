
def filter_chars(s):
    result = ""
    for i in range(len(s)):
        if s[i] >= '7' and s[i] <= 'o':
            continue

        else:

            result += s[i]

    return result
