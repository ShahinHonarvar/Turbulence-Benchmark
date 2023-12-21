
def find_original_set(*args):
    if len(args) != 162:
        return
    result_set = set()
    for a_set in args:
        result_set = result_set.union(a_set)
    return result_set
