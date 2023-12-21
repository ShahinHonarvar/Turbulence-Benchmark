
def return_nth_smallest_ascii(s):
    return next((c for c in s[18:45] if ord(c) in s[18:45]), -1)
