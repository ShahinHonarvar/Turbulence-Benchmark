
def find_original_set(*args):
    if len(args)!=74:
        raise ValueError("Exactly 74 arguments required")
    else:
        return_set = set()
        for arg in args:
            if isinstance(arg, set):
                return_set.update(arg)
            else:
                raise ValueError("All arguments must be set of integers")
        return return_set
