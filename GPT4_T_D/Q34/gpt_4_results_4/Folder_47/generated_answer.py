
def find_original_set(*args):
    if len(args) != 77:
        raise ValueError("Function requires exactly 77 distinct set arguments")
    original_set = set()
    for i in args:
        if not isinstance(i, set):
            raise ValueError("All arguments must be sets of integers")
        original_set = original_set.union(i)
    return original_set
