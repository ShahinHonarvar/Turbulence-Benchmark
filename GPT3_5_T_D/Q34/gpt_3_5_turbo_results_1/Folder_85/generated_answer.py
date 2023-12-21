
def find_original_set(*args):
    result = args[0]
    for arg in args[1:]:
        result |= arg
    return result
