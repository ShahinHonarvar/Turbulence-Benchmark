
def return_nth_smallest_ascii(string):
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[0])
    nth_smallest_ascii = sorted_chars[7][0]
    return nth_smallest_ascii
