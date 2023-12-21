
def find_original_set(*args):
    result_set = set()
    for arg in args:
        result_set = result_set.union(arg)
    return result_set
