
def find_original_set(*args):
    result_set = set()
    for each_set in args:
        result_set.update(each_set)
    return result_set
