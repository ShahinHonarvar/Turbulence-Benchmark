
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'(?i)[a-z]{13}', s) if p == p[::-1]}
