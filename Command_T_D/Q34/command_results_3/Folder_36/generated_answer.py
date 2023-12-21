import sys
def find_original_set(S):
    # Create a set that contains all the elements of S
    s = set(S)
    # Remove all the elements from s that appear in more than one set
    s = {e for e in s if len(s) == 1}
    # For each element in s, add all the elements that appear in S with it
    s = {e | {e for s in S for e in s if e == s} for e in s}
    # Return s
    return s
