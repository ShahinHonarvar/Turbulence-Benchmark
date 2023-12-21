
def find_original_set(*args):
    final_set = set()
    if len(args) != 78:
        raise ValueError("Please provide exactly 78 arguments.")
    else:
        for arg in args:
            final_set.update(set(arg))
    return final_set
