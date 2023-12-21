
def return_nth_smallest_ascii(string):
    char_count = {}
    for i in range(15, 22):
        char_count[string[i]] = char_count.get(string[i], 0) + 1
    sorted_chars = sorted(char_count.items(), key=lambda x: (x[1], x[0]))
    return sorted_chars[5][0]
