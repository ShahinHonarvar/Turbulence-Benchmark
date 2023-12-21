
def find_original_set(*args):
    if len(args) != 68:
        return "Exactly 68 sets are expected."
    else:
        original_set = set()
        for arg in args:
            original_set.update(arg)
        return original_set
