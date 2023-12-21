
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'(?i)[a-zA-Z]{54}', s) if p == p[::-1]}
