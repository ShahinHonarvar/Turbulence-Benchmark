
def palindrome_of_length_n(s):
    return {p for p in s if len(p) == 35 and p[::-1].isalpha()}
