
def find_original_set(*args):
    if len(args) != 57:
        print("Error: You need to input exactly 57 sets.")
        return None
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
