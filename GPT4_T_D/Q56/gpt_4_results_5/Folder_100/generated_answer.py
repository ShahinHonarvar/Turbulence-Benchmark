
def all_substring_of_size_n(s):
    n = 92
    substrings = set()
    for i in range(0, len(s)-n+1):
        substring = s[i:i+n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)
