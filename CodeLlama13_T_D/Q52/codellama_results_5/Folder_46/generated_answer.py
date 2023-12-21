
def palindrome_of_length_n(s):
    return {p for p in (s[i:i+464] for i in range(len(s)-463)) if p == p[::-1]}
