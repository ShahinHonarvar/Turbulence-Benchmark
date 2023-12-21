
def all_substring_of_size_n(s):
    n = 50
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n and all(substring.count(c) == 1 for c in substring):
            result.append(substring)
    return result
