def find_original_set(s):
    s.sort()
    for i in range(1, len(s)):
        s[i] = s[i].union(s[i - 1])
    return s[0]
