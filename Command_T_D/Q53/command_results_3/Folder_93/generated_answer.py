def palindrome_of_length_at_least_n(s):
    return set(s[i:i+90] for i in range(len(s)-90))
