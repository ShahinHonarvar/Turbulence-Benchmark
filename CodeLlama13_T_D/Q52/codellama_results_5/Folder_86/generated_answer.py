
def palindrome_of_length_n(s):
    return {p for p in (''.join(c) for c in itertools.combinations(s, 181)) if p == p[::-1]}
