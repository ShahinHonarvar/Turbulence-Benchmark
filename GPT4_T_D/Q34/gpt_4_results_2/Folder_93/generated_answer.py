
def find_original_set(*args):
    if len(args) != 90:
        raise ValueError("Function requires exactly 90 distinct sets as arguments.")

    original_set = set()

    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments must be of type set.")
        else:
            original_set = original_set.union(arg)

    return original_set
