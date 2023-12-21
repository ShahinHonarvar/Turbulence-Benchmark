
def find_original_set(*args):
    original_set = set()
    if len(args) != 993:
        return "The function takes exactly 993 distinct arguments."
    else:
        for each_set in args:
            original_set = original_set.union(each_set)
    return original_set
