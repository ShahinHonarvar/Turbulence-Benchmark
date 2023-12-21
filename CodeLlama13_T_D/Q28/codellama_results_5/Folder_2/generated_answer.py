
def return_nth_smallest_ascii(s):
    count = {}
    for c in s:
        if ord(c) >= 48 and ord(c) <= 76:
            count[c] = count.get(c, 0) + 1
    
    return sorted(count, key=lambda x: (count[x], ord(x)))[4]
