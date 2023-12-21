def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 145):
        result.append(s[i:i + 146])
    return result
