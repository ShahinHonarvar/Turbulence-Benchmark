def palindrome_of_length_at_least_n(s):
    return set(i for i in s.lower() if i[::-1] == i)
