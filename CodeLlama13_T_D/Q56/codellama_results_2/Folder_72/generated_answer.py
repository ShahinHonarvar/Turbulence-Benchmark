
def all_substring_of_size_n(s):
    n = 88
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n and not any(substring in r for r in result):
            result.append(substring)
    return result
