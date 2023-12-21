def palindrome_of_length_n(s):
    return set(x for x in s.lower() if len(x) == 90 and x[::-1] == x)
