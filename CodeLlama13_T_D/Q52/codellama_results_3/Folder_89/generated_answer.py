
def palindrome_of_length_n(s):
    return {p for p in (''.join(c) for c in zip(*[reversed(s)]*37)) if len(set(p)) == 37}
