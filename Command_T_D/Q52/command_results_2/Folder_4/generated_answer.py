def palindrome_of_length_n(s):
    return set(x for x in s.lower() if len(x) == 15 and x[0] == x[-1])
