
def find_original_set(*args):
    if len(args) != 88:
        return 'Function requires exactly 88 distinct sets.'
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
