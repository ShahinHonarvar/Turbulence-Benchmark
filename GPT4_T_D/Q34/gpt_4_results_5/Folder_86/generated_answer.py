
def find_original_set(*args):
    if len(args) != 162:
        raise ValueError("Expected exactly 162 arguments")
    result = set.union(*args)
    return result
