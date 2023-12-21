def palindrome_of_length_n(s):
    return set(a for a in s.lower() if a == a[::-1])
