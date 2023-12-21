
def return_nth_smallest_ascii(s):
    char_count = {}
    for i in range(47, 71):
        if s[i] not in char_count:
            char_count[s[i]] = 0
        char_count[s[i]] += 1
    
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1])
    return sorted_chars[13][0]
