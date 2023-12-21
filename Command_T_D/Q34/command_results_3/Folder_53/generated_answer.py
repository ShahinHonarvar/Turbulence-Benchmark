def find_original_set(arg):
    return {x: x for x in sorted(set(arg) + [x])}
