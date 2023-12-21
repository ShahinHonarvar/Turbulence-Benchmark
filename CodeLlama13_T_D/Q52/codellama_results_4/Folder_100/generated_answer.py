
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'[A-Za-z]{91}', s, flags=re.I) if p == p[::-1]}
