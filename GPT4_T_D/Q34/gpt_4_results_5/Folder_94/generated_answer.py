
def find_original_set(*args):
     if len(args) != 69:
         raise Exception("You must provide exactly 69 sets")
     original_set = set()
     for s in args:
         original_set = original_set.union(s)
     return original_set
