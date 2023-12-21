
def find_original_set(*args):
    if len(args) != 38:
        raise ValueError("Function requires exactly 38 arguments")
    
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
