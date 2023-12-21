def find_original_set(*args) -> set[int]:
    result = set()
    for s in args:
        result |= s
    return result