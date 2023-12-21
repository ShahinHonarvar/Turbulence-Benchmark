
def find_original_set(*args):
    if len(args) != 42:
        raise ValueError("Exactly 42 arguments are needed")

    original_set = set()

    for subset in args:
        if not isinstance(subset, set):
            raise TypeError("All arguments must be sets")

        original_set = original_set.union(subset)

    return original_set
