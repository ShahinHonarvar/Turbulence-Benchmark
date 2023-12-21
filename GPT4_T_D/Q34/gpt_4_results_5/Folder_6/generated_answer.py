
def find_original_set(*args):
    if len(args) != 276:
        raise ValueError("The function takes exactly 276 distinct arguments")

    return set.union(*args)
