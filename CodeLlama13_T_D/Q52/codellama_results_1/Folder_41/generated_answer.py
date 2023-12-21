
def palindrome_of_length_n(string):
    return {s[::-1].lower() for s in string if len(s) == 60 and all(c.isalpha() for c in s)}
