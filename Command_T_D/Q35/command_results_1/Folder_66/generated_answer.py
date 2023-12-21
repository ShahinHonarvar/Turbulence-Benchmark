import itertools
def remove_repeat_chars(s):
    for c in itertools.permutations(s[11:-76]):
        yield c
