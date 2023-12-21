
def all_substring_of_size_n(s):
    substrings = set()
    n = 127
    for i in range(len(s)):
        if i+n <= len(s) and len(set(s[i:i+n])) == n:
            substrings.add(s[i:i+n])
    return list(substrings)
