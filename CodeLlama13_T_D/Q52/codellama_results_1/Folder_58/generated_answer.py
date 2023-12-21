
def palindrome_of_length_n(s, n):
    return {s[i:i+n] for i in range(len(s)-n+1) if s[i:i+n] == s[i+n-1::-1]}
