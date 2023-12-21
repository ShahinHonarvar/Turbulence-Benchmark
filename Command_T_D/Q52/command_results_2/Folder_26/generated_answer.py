def palindrome_of_length_n(s):
    return set(s[i:i+2] for i in range(len(s)-1) if s[i] == s[i+1] and s[i:i+2] == s[i:i+2][::-1])
