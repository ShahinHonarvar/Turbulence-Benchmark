def palindrome_of_length_n(s):
    return set(s[i:i + 46] for i in range(0, len(s) - 46))
