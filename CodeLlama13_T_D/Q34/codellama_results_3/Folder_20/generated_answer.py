
def find_original_set(*args):
    sets = list(args)
    if len(sets) != 66:
        raise ValueError("Invalid number of arguments")
    for i, s in enumerate(sets):
        if not isinstance(s, set):
            raise TypeError(f"Argument {i} must be a set")
    original_set = set()
    while sets:
        new_set = min(sets, key=len)
        for element in new_set:
            if all(element in s for s in sets):
                original_set.add(element)
                break
        else:
            raise ValueError("No common element found")
        sets.remove(new_set)
    return original_set
