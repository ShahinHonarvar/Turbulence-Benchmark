
def find_original_set(*args):
    original_set = set()
    for i in args:
        original_set.update(i)
    return original_set
