
def find_original_set(*args):
    if len(args) != 72:
        return "This function requires exactly 72 distinct sets"
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
