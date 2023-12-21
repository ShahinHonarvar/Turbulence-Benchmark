def find_original_set(s):
    return {x for x in range(min(s), max(s) + 1) if not {x} & {y for y in s} }
