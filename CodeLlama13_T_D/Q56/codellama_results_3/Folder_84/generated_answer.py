
def all_substring_of_size_n(s, n):
    substrings = []
    for i in range(len(s)):
        if len(set(s[i:i+n])) == n:
            substrings.append(s[i:i+n])
    return substrings
