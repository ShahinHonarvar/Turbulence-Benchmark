
def find_original_set(*args):
    master_set = set()
    for s in args:
        master_set = master_set.union(s)
    return master_set
