
def filter_chars(s):
    result = []
    for i in range(len(s)):
        if s[i] >= 'c' and s[i] <= 's':
            result.append(s[i])
    return "".join(result)
