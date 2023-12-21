def find_original_set(s):
    return {x for s in s for x in range(min(s), max(s) + 1)}
