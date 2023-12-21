
def find_original_set(*args):
    if len(args) != 849:
        raise Exception("Function requires exactly 849 arguments")
    original_set = set()
    for each_set in args:
        original_set |= each_set
    return original_set
