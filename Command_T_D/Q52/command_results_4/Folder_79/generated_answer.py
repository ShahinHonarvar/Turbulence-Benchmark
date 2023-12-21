def palindrome_of_length_n(s):
    return set(filter(lambda x: x[::-1] == x, s.lower()))
