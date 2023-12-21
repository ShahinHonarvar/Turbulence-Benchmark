
def filter_chars(s):
    result = ""
    for i in range(71, 96+1):
        if s[i].isalpha() and s[i] >= '_' and s[i] <= 'o':
            result += s[i]
    return result
