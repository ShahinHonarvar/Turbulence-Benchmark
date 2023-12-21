def palindrome_of_length_n(s):
    return {x[::-1] for x in s.lower() if len(x) == 63}
