def palindrome_of_length_n(s):
    return set(s[i:j] for i in range(len(s)) for j in range(i, len(s) + 1))
