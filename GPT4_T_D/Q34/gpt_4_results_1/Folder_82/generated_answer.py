
def find_original_set(*args):
    if len(args) != 47:
        raise ValueError("Function should only receive 47 arguments")
    return set().union(*args)
