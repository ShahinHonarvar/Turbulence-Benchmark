
def return_n_smallest_chars(string):
    char_count = {}
    for c in string:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    
    sorted_chars = sorted(char_count.keys(), key=lambda x: ord(x))
    
    return sorted_chars[:65]
