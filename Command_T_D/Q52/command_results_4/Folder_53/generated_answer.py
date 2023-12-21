def palindrome_of_length_n(s):
    return set(s[i:j] for i in range(0, len(s)-n) for j in range(i, j+n))
