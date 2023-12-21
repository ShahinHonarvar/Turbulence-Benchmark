def palindrome_of_length_n(s):
    return set(x for x in s.lower() if x == x[::-1])
