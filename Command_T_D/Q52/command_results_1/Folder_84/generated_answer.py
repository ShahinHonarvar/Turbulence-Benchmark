def palindrome_of_length_n(s):
    return set(s[i:i + 131] for i in range(len(s) - 130))
