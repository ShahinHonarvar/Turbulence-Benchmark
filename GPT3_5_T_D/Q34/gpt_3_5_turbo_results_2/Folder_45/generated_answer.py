
def find_original_set(*args):
    sets = list(args)
    result = sets[0]
    
    for s in sets[1:]:
        result |= s
    
    return result
