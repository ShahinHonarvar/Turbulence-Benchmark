
def find_original_set(*args):
    if len(args) != 985:
        raise ValueError("Function requires 985 arguments.")
    else:
        original_set = set()
        for arg in args:
            original_set = original_set.union(arg)
        return original_set
