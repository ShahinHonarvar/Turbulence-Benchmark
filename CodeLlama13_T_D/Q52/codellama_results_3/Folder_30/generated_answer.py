
def palindrome_of_length_n(s, n):
    return {s[i:i+n] for i in range(len(s)-n) if s[i:i+n].lower() == s[i:i+n][::-1].lower()}
