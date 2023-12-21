
def palindrome_of_length_n(s):
    return {p for p in re.findall('(?i)[a-z]{279}', s) if p == p[::-1]}
