def palindrome_of_length_n(s):
    return set(filter(lambda x: x == s[::-1], s))
