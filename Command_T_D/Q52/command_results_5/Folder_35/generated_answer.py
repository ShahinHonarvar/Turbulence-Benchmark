def palindrome_of_length_n(s):
    return set(a for a in (s[i:i+116] for i in range(len(s) - 115)) if a[0] == a[-1] and all(c.islower() for c in a))
