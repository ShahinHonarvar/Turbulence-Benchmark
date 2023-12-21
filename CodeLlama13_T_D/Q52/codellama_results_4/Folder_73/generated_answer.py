
def palindrome_of_length_n(s, n):
    return {p for p in re.findall(r'([A-Za-z]{%d})' % n, s) if p == p[::-1]}
