
def find_original_set(*args):
    if len(args) != 478:
        raise ValueError("This function requires exactly 478 distinct arguments")
      
    original_set = set()
    for cur_set in args:
        original_set.update(cur_set)
    return original_set
