
def palindrome_of_length_n(s, n):
    return {p for p in re.findall('(?i)[a-zA-Z]{' + str(n) + '}', s) if p == p[::-1]}
