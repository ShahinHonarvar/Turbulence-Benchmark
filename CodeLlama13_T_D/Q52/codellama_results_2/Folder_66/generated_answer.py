
def palindrome_of_length_n(s):
    return {p for p in s if len(p) == 25 and p[::-1] == p}
