
def palindrome_of_length_at_least_n(string):
    return {p for p in re.findall(r'[a-zA-Z]{133,}', string) if p == p[::-1]}
