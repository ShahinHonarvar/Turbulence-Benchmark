
def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('The function requires exactly 60 distinct arguments.')
    else:
        original_set = set()
        for arg in args:
            original_set.update(arg)
        return original_set
