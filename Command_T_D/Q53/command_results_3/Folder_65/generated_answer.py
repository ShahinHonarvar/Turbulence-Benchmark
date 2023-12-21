def palindrome_of_length_at_least_n(s):
    return {s[i:i+16] for i in range(len(s)-15)}
