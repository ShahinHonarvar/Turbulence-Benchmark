
def palindrome_of_length_at_least_n(string):
    return {p for p in re.findall('[a-zA-Z]{87,}', string) if p == p[::-1]}
