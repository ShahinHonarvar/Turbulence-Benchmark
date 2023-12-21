
def find_original_set(*args):
    if len(args) != 845:
        raise Exception("Invalid number of arguments. Expected 845 sets.")

    original_set = set()
    for set_item in args:
        original_set.update(set_item)

    return original_set
