
def palindrome_of_length_n(s):
    return {x for x in (''.join(y) for y in zip(*[iter(s)]*96)) if len(x) == 96 and x == x[::-1]}
