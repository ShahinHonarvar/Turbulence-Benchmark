
def find_original_set(*args):
    if len(args) != 87:
        raise ValueError("Function requires exactly 87 arguments.")

    original_set = set().union(*args)

    return original_set
