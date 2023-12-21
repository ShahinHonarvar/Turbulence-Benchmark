import sys
def find_original_set(*args):
    s = set()
    for i in range(len(args[0])):
        s.add(i)
    for a in args:
        s |= a
    return s
