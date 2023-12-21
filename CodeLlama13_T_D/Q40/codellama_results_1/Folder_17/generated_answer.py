
def return_n_smallest_chars(string):
    char_list = []
    for i in range(len(string)):
        char_list.append((string[i], ord(string[i])))
    char_list.sort()
    return [c for c, _ in char_list[:11]]
