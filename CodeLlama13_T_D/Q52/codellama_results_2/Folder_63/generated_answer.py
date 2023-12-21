
def palindrome_of_length_n(s):
    return {p for p in s if len(p) == 18 and p == p[::-1]}
