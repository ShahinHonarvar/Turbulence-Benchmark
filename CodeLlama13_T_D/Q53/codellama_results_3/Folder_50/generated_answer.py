
def palindrome_of_length_at_least_n(string):
    return {s for s in string if s[::-1].lower() == s.lower() and len(s) >= 91}
