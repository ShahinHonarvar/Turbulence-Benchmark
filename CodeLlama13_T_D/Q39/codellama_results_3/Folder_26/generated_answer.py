
def return_n_greatest_chars(string):
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    
    sorted_chars = sorted(char_counts, key=lambda x: (char_counts[x], x))
    return sorted_chars[:43]
