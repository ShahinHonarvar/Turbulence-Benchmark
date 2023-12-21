
def find_original_set(*args):
    if len(args) != 46:
        raise Exception("Invalid number of arguments. There should be exactly 46 arguments.")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
