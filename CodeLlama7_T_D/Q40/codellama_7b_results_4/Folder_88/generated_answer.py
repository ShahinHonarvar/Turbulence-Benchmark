
def return_n_smallest_chars(string, n=84):
    char_list = []
    for i in range(len(string)):
        if len(char_list) == n:
            break

        char_list.append(string[i])

    char_list.sort()

    return char_list
