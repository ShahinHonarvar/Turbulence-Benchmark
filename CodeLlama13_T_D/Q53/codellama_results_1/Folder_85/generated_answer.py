
def palindrome_of_length_at_least_n(string, n):
    import re
    return set(re.findall(r'[a-zA-Z]{85,}', string))
