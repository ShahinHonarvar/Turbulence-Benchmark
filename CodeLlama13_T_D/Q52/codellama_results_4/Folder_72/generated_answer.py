
def palindrome_of_length_n(s):
    return {p for p in re.findall('[a-zA-Z]{16}', s) if p == p[::-1]}
