
def find_original_set(*args):
    if len(args) != 15:
        raise Exception("Function must take exactly 15 arguments")

    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)

    return original_set
