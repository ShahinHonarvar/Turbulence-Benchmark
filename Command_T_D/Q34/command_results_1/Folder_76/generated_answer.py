import itertools
def find_original_set(s):
    return {i for s in s for i in itertools.chain.from_iterable(s)}
