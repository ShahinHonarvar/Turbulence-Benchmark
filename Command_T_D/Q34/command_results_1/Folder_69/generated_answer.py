def find_original_set(arg):
    # Code by Kevinpoint85
    # Check if any set in the list of sets is a superset of all the others
    # If so, return that set, otherwise return the empty set
    if all(set(arg).issuperset(set(arg[0]))):
        return set(arg[0])
    else:
        return set()
