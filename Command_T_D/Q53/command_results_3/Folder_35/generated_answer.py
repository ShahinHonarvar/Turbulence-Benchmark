def palindrome_of_length_at_least_n(s):
    return set(s.lower() for i in range(len(s) + 1)) & {w for w in range(26, 0, -1) if w*2 <= len(s) and s[w-1] == s[w*2-1]}
