import itertools
def find_original_set(s):
    return {k: list(set(v)) for k, v in itertools.groupby(s)}
