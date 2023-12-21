
def find_original_set(*args):
    if len(args) != 790:
        return "Please provide 790 distinct arguments"
    
    smallest_set = set()
    for each_set in args:
        smallest_set.update(each_set)
        
    return smallest_set
