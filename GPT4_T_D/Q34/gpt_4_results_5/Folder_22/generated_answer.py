
def find_original_set(*args):
    if len(args) != 24:
        return "Function takes exactly 24 distinct sets as arguments"
    else:
        final_set = set()
        for arg in args:
            final_set = final_set.union(arg)
        return final_set
