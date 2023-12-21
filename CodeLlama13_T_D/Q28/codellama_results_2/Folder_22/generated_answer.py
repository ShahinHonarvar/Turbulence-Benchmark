
def return_nth_smallest_ascii(string):
    char_count = {}
    for i in range(0, 17):
        if string[i] not in char_count:
            char_count[string[i]] = 1
        else:
            char_count[string[i]] += 1
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[0])
    return sorted_char_count[16][0]
