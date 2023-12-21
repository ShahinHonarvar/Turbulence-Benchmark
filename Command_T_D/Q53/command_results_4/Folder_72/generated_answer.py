def palindrome_of_length_at_least_n(s):
    return set(s[i:j] for i in range(0, len(s)-88) for j in range(i, len(s)-1))
