
def find_original_set(*args):
    if len(args) != 91:
        raise ValueError("Expected 91 arguments")
    result_set = set()
    for arg in args:
        result_set = result_set.union(arg)
    return result_set
