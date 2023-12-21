
def all_substring_of_size_n(s):
    n = 11
    substr = []
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        if not any(c in sub for c in substr):
            substr.append(sub)
    return substr
