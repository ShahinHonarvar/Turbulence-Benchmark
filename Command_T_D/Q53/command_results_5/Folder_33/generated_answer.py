def palindrome_of_length_at_least_n(s):
    return {s[i:i + 2 * n] for i in range(0, len(s) - n) for n in range(1, 150)}
