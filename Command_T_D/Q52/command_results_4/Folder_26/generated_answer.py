def palindrome_of_length_n(s):
    return set(s[i:i+366] for i in range(len(s)-365))
