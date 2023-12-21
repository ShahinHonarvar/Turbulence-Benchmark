
def palindrome_of_length_at_least_n(string, n):
    return set(re.findall(r'(?i)[a-zA-Z]{112,}', string))
