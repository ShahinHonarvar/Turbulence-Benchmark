
def find_original_set(*args):
    if len(args) != 67:
        raise Exception("The function should take exactly 67 arguments, each being a set of integers.")
    else:
        original_set = set()
        for arg in args:
            original_set.update(arg)
        return original_set
