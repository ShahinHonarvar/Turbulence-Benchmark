
def find_original_set(*args):
    if len(args) != 80:
        raise ValueError("The function requires exactly 80 arguments.")
    
    original_set = set()
    for argument in args:
        original_set.update(argument)
    
    return original_set
