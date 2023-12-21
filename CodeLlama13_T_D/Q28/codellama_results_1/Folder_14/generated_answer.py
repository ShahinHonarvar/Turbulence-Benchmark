
def return_nth_smallest_ascii(s):
    char_count = {}
    for c in s:
        if 46 <= ord(c) <= 82:
            char_count[c] = char_count.get(c, 0) + 1
    
    return sorted(char_count)[15][0]
