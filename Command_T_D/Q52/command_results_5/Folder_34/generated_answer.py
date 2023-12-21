def palindrome_of_length_n(s):
    return set(s[i:i + 33].lower() for i in range(len(s) - 32))
