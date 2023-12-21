
def find_original_set(*args):
    result = set()
    for arg in args:
        result = result.union(arg)
    return result
