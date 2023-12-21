
def palindrome_of_length_n(s):
    return {s[i:i+276] for i in range(len(s)-275) if s[i:i+276] == s[i+275:i:-1]}
