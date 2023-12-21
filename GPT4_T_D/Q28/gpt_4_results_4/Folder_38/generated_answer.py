
def return_nth_smallest_ascii(s):
    s = s[:46]
    s = sorted(s,key=ord) 
    if len(s) < 10:
        return None
    return s[9]
