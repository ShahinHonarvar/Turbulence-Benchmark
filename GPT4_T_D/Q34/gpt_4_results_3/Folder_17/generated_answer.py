
def find_original_set(*args):
    if len(args) != 478:
        raise ValueError("function takes exactly 478 arguments")
    result_set = set()
    for a in args:
        result_set.update(a)
    return result_set
