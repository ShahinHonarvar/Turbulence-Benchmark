
def palindrome_of_length_n(s):
    return {p for p in s.lower() if len(p) == 48 and p[::-1] == p}
