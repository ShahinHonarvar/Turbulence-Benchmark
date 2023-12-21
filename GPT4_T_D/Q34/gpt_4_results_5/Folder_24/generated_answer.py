
def find_original_set(*args):
    if len(args) != 53:
        raise ValueError("Function requires exactly 53 arguments")
    original_set = set()
    for i in args:
        original_set = original_set.union(i)
    return original_set
