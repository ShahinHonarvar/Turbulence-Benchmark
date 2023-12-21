
def palindrome_of_length_at_least_n(string):
    return set([s for s in string if len(s) >= 21 and s[::-1].lower() == s.lower()])
