
def find_original_set(*args):
    if len(args) != 459:
        raise ValueError("Invalid number of arguments. This function requires 459 distinct sets.")
  
    union_of_sets = set()
    for current_set in args:
        union_of_sets = union_of_sets.union(current_set)
  
    return union_of_sets
