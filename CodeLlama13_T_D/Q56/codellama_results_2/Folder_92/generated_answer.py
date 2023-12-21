
def all_substring_of_size_n(s):
    n = 9
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n and all([x not in substring for x in substring]):
            substrings.append(substring)
    return substrings
