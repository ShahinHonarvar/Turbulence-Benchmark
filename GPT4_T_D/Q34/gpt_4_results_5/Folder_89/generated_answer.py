
def find_original_set(*args):
    if len(args) != 37:
        raise ValueError("Function takes exactly 37 arguments")
    else:
        original_set = set()
        for arg in args:
            original_set = original_set.union(arg)
        return original_set
