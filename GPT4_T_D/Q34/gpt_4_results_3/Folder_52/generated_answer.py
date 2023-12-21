
def find_original_set(*args): 
    if len(args) != 746: 
        raise ValueError("Wrong number of arguments")
    total_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError("All arguments must be sets")
        total_set.update(arg)
    return total_set
