
def find_original_set(*args):
    if len(args) != 57:
        print('Error: Invalid number of arguments. Expected 57, got ' + str(len(args)))
        return
    original_set = set()
    for i in args:
        original_set.update(i)
    return original_set
