
def palindrome_of_length_at_least_n(string):
    return {s for s in re.findall(r'\b[a-zA-Z]{11,}\b', string) if s == s[::-1]}
