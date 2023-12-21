
def return_nth_smallest_ascii(s):
    return next((c for c in s[0:45] if ord(c) in s[0:45] and ord(c) < ord(s[46])), s[45])
