
def all_substring_of_size_n(s):
    if len(s) < 100:
        return []
    result = []
    for i in range(len(s)-99):
        substr = s[i:i+100]
        if len(set(substr)) == 100:
            result.append(substr)
    return result
