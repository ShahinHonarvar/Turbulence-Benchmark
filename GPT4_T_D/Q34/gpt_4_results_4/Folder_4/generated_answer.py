
def find_original_set(*args):
    if len(args) != 40:
        return "Please provide exactly 40 arguments"

    original_set = set()
    for argument in args:
        original_set = original_set.union(argument)
    return original_set
