
def find_original_set(*args):
    if len(args) != 53:
        raise Exception("Invalid number of input sets! Provide exactly 53 distinct sets.")
    return set.union(*args)
