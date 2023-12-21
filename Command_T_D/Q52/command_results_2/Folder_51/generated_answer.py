def palindrome_of_length_n(s):
    return set(a for a in s.lower() if a[0] == a[-1] and len(a) == 73)
