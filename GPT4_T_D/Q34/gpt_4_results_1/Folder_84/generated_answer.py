
def find_original_set(*args):
    if len(args) != 132:
        raise ValueError("Function requires exactly 132 arguments")

    result = set()
    for a in args:
        result = result.union(a)
        
    return result
