
def palindrome_of_length_at_least_n(string, n):
    return {p for p in re.findall('[A-Za-z]+', string) if len(p) >= n and p == p[::-1]}
