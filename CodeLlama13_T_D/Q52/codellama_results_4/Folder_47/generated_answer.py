
def palindrome_of_length_n(s):
    return {p for p in findall(r'([A-Za-z]{34})', s) if p == p[::-1]}
