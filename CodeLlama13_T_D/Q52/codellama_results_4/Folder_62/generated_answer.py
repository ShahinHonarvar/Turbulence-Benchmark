
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'[a-z]{188}', s, flags=re.I) if p == p[::-1]}
