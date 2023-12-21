
def return_nth_smallest_ascii(s):
    lst = sorted(list(set(s[:7])), key=lambda x: ord(x))
    return lst[6]
