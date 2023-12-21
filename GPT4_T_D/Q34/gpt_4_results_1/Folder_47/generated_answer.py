
def find_original_set(*args):
    if len(args) != 77:
        raise ValueError("The function requires exactly 77 arguments")
    original_set = set()
    for i in args:
        original_set = original_set.union(i)
    return original_set
