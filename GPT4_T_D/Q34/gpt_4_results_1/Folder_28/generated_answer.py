
def find_original_set(*args):
    if len(args) != 43:
        return "Must provide exactly 43 distinct arguments"
    else:
        original_set = set()
        for arg in args:
            original_set.update(arg)
        return original_set
