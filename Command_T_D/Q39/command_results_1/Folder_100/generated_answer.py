import itertools
def return_n_greatest_chars(s):
    return sorted(list(itertools.permutations(s)), key=lambda x: x[0], reverse=True)[:72]
