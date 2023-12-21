
def find_original_set(*args):
    if len(args) != 162:
        return 'Error: function requires 162 arguments.'
    
    original_set = set()
    for arg in args:
        original_set.update(arg)

    return original_set
