import itertools
def find_original_set(X):
    # Create the powerset of X
    # and filter it to only contain
    # the unique elements of X
    # This gives us all possible
    # original sets
    original_sets = set(
        itertools.chain.from_iterable(
            itertools.permutations(X)
        )
    )
    return min(original_sets, key=lambda x: x)
