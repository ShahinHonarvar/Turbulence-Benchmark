
def find_original_set(*args):
    original_set = set()
    for i in range(len(args)):
        original_set = original_set.union(args[i])
    return original_set
