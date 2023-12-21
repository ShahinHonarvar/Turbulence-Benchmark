
def all_substring_of_size_n(s):
    substrings = set()
    n = 97
    for i in range(len(s)):
        if len(set(s[i:i+n])) == n:
            substrings.add(s[i:i+n])
    return list(substrings)
