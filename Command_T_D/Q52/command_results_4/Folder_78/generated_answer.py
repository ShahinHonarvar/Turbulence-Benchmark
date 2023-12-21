def palindrome_of_length_n(s):
    return set(i for i in s.lower() if i == i[::-1])
