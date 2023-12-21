
def find_original_set(*args):
    if len(args) != 247:
        raise ValueError("The function should receive exactly 247 arguments.")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
