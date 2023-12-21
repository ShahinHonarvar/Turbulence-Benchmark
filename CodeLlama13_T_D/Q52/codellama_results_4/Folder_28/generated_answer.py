
def palindrome_of_length_n(s):
    return {p for p in (s[i:i+43] for i in range(len(s) - 42)) if p == p[::-1]}
