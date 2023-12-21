
def return_n_smallest_chars(string):
    char_counts = {}
    for c in string:
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1
    
    sorted_chars = sorted(char_counts, key=lambda x: ord(x))
    return sorted_chars[:87]
