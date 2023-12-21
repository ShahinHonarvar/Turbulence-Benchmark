
def find_original_set(*args):
    if len(args) != 312:
        raise ValueError("The function expects exactly 312 arguments")
    
    original_set = set()
    for s in args:
        original_set.update(s)

    return original_set
