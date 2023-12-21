
def find_original_set(*args):
    if len(args) != 66:
        return "Invalid number of arguments"
    else:
        original_set = set()
        for argument in args:
            original_set = original_set.union(argument)
        return original_set
