def palindrome_of_length_at_least_n(s):
    return set(filter(lambda x: len(x)>=13 and x==x[::-1], s.lower()))
