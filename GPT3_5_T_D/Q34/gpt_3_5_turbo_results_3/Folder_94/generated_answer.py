
def find_original_set(*args):
    result = set()
    for s in args:
        result.update(s)
    return result
