def palindrome_of_length_at_least_n(s):
    return set(filter(str.isalpha, (x for x in s.lower() if len(x)>=112 and x[::-1]==x))
