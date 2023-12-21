
def palindrome_of_length_at_least_n(s):
    return {p for p in re.findall(r'[a-zA-Z]{20,}', s) if p == p[::-1]}
