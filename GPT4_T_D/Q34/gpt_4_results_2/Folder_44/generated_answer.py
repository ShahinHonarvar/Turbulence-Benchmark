
def find_original_set(*args):
    if len(args) != 926:
        return "The function requires exactly 926 arguments!"
    else:
        original_set = set()
        for arg in args:
            if isinstance(arg, set):
                original_set = original_set.union(arg)
            else:
                return "All arguments should be sets!"
        return original_set
