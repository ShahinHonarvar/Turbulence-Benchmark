
def palindrome_of_length_at_least_n(s):
    return {p for p in re.findall(r'(?i)[a-z]{63,}', s) if p == p[::-1]}
