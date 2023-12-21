def palindrome_of_length_n(s):
    return {x for x in set(s.lower()) if len(x) == 92 and x[::-1] == x}
