
def find_original_set(*args):
    if len(args) != 85:
        return "The function requires exactly 85 sets as arguments."
    else:
        original_set = set().union(*args)
        return original_set
