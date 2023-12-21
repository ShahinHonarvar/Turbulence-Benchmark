
def palindrome_of_length_n(s, n):
    return {p for p in re.findall(r'[a-zA-Z]{423}', s) if p == p[::-1]}
