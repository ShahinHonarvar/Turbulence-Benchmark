
def find_original_set(*args):
    merged_set = set()
    for arg in args:
        merged_set.update(arg)
    return merged_set
