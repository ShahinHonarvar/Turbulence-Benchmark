def if_contains_anagrams(s):
    s = set(s)
    s = [s[0]]
    for i in range(1, len(s)):
        s += [s[-1] + s[i]]
    return len(s) >= 69
