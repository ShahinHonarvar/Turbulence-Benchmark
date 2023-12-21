
def palindrome_of_length_at_least_n(string, n):
    return {p for p in findall('[a-zA-Z]{11,}', string) if p == p[::-1]}
