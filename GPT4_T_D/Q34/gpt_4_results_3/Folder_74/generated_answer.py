
def find_original_set(*args):
    if len(args) != 96:
        raise ValueError("You must provide exactly 96 sets.")
    return_set = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError("All arguments must be of type set.")
        return_set.update(s)
    return return_set
