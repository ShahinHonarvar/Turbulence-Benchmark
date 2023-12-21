
def palindrome_of_length_at_least_n(s):
    return {p for p in re.findall(r'\b[a-zA-Z]{13,}\b', s) if p == p[::-1]}
