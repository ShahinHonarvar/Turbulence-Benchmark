import sys
def find_original_set(s):
    s.sort()
    # initializing empty set and stack
    sets = set()
    stk = []
    # searching for original set
    for x in s:
        # if current set is not in the stack, then it is added to the set
        if x not in stk:
            sets.add(x)
            stk.append(x)
        # else, if current set is in the stack, then we do nothing
        else:
            pass
    return sets
