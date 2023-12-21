
def find_original_set(*args):
    if len(args) != 51:
        return "Error: function requires exactly 51 distinct arguments"

    return set().union(*args)
