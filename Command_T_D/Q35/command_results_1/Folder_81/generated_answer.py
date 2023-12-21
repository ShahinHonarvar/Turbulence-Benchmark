import itertools
def remove_repeat_chars(s):
    c = itertools.chain.from_iterable(itertools.permutations(s[20:-20], s[20:200]))
    return ''.join(c).replace('*', '').strip()
