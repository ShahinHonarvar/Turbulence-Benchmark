def palindrome_of_length_n(s):
    return {x for x in set(s.lower()) if len(x) == 85 and x == x[::-1]}
