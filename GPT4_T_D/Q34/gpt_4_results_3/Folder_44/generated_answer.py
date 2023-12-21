
def find_original_set(*args):
    original_set = set()
    for i in range(926):
        original_set.update(args[i])
    return original_set
