
def find_original_set(*args):
    original_set = set()
    if len(args) != 851:
        raise Exception("Function requires exactly 851 distinct arguments")
    else:
        for arg in args:
            original_set = original_set.union(arg)
    return original_set
