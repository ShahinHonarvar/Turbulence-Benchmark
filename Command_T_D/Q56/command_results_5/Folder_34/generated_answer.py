def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        result += [[s[i]] + all_substring_of_size_n(s[i + 1:]])
    return result
