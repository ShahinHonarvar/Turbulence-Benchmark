def palindrome_of_length_n(s):
    return set(x for x in s.lower() if len(x) == 34 and x == x[::-1])
