
def all_substring_of_size_n(s):
    n = 73
    result = []
    for i in range(len(s) - n + 1):
        substr = s[i:i+n]
        if len(set(substr)) == n:
            if substr not in result:
                result.append(substr)
    return result
