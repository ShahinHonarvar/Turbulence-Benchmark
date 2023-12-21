
def find_original_set(args):
    return set(min(itertools.chain(*args), key=len))
