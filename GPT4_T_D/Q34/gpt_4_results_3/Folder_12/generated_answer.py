
def find_original_set(*args):
    if len(args) != 51: 
        return "The function takes 51 distinct arguments"
    else:
        original_set = set().union(*args)
    return original_set
