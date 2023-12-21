
def return_nth_smallest_ascii(string):
    char_counts = {}
    for i in range(20, 31):
        if string[i].isalpha():
            char_counts[string[i]] = char_counts.get(string[i], 0) + 1
    
    sorted_chars = sorted(char_counts.keys(), key=lambda x: ord(x))
    return sorted_chars[7]
