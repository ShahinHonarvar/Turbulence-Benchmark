
def find_original_set(*args):
    if len(args) != 20:
        return "The function should take 20 arguments"
    else:
        original_set = set()
        for arg in args:
            original_set.update(arg)
        return original_set
