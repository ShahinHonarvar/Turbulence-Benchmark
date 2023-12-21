
def all_substring_of_size_n(s):
    n = 58
    substrings = []
    for i in range(0, len(s)):
        if len(s[i:i + n]) == n and len(set(s[i:i + n])) == n:
            substrings.append(s[i:i + n])
    return list(set(substrings))
