
def palindrome_of_length_at_least_n(s):
    return {p for p in re.findall(r'(?i)[a-z]{62,}', s) if p == p[::-1]}
