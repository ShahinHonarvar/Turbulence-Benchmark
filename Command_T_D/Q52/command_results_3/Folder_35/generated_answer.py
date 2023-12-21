def palindrome_of_length_n(s):
    return set(p for p in s.lower() if len(p) == 116 and p == p[::-1])
