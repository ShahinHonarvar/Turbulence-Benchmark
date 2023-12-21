
def palindrome_of_length_at_least_n(string, n):
    return {p for p in re.findall(r'[a-zA-Z]{122,}', string) if p == p[::-1]}
