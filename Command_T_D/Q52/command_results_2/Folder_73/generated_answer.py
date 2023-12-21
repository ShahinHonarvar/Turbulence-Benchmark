def palindrome_of_length_n(s):
    return set(map(str.lower, filter(str.isalpha, str(range(0, len(s) - 1)))))
