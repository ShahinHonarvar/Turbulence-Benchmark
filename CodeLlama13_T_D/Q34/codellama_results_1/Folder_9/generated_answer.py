
def find_original_set(arg1, arg2, ..., arg73):
    return {x for x in range(min(arg1), max(arg73)) if all(x in a for a in (arg1, arg2, ..., arg73))}
