
def find_original_set(*args):
    if len(args) != 87:
        raise ValueError("Function only accepts 87 set arguments.")
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set
