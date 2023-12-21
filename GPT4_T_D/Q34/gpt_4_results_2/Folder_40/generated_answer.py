
def find_original_set(set_arg):
    min_val = min(set_arg)
    max_val = max(set_arg)
    return set(range(min_val, max_val+1))
