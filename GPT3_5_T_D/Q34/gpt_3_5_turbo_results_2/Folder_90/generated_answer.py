
def find_original_set(*args):
    result = set()
    for arg in args:
        result.update(arg)
    return result
