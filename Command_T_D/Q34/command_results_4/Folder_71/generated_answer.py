import itertools
def find_original_set(S):
    return min(set(x for x in itertools.chain(*S)), key=lambda x: len(x))
