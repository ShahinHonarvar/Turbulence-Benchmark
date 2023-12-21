def all_substring_of_size_n(s):
    result = []
    for c in s:
        if len(result) == 49:
            break
        result += [c * 49]
    return result
