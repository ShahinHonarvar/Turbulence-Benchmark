import itertools
def all_substring_of_size_n(s):
    for ss in itertools.permutations(s):
        if len(ss) == 56:
            yield ss
