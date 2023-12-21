
def find_original_set(*args):
    if len(args) != 19:
        raise Exception('Expected exactly 19 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise Exception('All arguments must be sets')
        original_set = original_set.union(arg)
    return original_set
