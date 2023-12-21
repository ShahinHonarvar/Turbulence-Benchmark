
def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 49 + 1):
        substring = s[i:i+49]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))
