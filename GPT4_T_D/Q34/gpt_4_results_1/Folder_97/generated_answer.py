
def find_original_set(*args):
    # check if the length of arguments is equal to 194
    if len(args) != 194:
        return ("Function requires exactly 194 arguments. "
                f"{len(args)} were given")
                
    # Merge all the sets
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
        
    return original_set
