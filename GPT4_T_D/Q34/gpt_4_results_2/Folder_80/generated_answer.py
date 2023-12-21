
def find_original_set(*args):
    if len(args) != 453:
        raise ValueError("Requires 453 distinct set arguments")
    result_set = set()
    for set_argument in args:
        result_set.update(set_argument)
    return result_set
