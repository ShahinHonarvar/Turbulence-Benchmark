
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'[a-zA-Z]{338}', s) if p == p[::-1]}
