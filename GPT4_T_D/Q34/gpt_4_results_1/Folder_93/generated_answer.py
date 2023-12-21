
def find_original_set(*args):
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set
