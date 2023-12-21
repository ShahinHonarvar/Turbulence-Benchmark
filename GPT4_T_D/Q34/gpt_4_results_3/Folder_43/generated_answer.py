
def find_original_set(*args):
    original_set = set()
    for each_set in args:
        original_set.update(each_set)
    return original_set
