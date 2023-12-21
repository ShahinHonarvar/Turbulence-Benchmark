
def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('Function requires exactly 67 arguments')
    result_set = set()
    for arg in args:
        result_set = result_set.union(arg)
    return result_set
