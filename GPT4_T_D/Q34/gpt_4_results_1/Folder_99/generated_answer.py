
def find_original_set(*args):
    if len(args) != 415:
        return "Error: Required number of arguments not supplied."
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            return "Error: All arguments must be sets."
        result = result.union(arg)
    return result
