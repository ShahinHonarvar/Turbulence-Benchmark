
def find_original_set(*args):
    if len(args) != 990:
        return "Error: Function requires exactly 990 distinct arguments"
    original_set = set()
    for argument in args:
        original_set.update(argument)
    return original_set
