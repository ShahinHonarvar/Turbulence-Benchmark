
def return_nth_smallest_ascii(string):
    char_count = {}
    for i in range(37, 60):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    
    return min(char_count.keys(), key=lambda x: (char_count[x], ord(x)))
