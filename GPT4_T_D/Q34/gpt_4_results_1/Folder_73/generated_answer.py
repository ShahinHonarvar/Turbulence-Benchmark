
def find_original_set(*args):
    if len(args) != 19:
        raise ValueError("Requires exactly 19 arguments")
    combined_set = set()
    for s in args:
        if not all(isinstance(i, int) for i in s):
            raise TypeError("All elements in all sets must be integers")
        combined_set.update(s)
    return combined_set
