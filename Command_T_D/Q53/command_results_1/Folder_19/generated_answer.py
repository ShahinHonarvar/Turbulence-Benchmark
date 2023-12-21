def palindrome_of_length_at_least_n(s):
    return set(s[i:i+24] for i in range(len(s)-23) if s[i:i+24] == s[i:i+24][::-1])
