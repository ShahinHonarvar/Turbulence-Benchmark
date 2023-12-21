def palindrome_of_length_n(s):
    return set(s[i:i + n] for i in range(len(s) - n) for n in range(1, min(len(s), 95) + 1))
