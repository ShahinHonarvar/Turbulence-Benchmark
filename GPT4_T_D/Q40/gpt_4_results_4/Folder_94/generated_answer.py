
def return_n_smallest_chars(char_string):
    if len(char_string) < 87:
        raise ValueError('The string must contain at least 87 distinct characters.')
    sorted_string = sorted(char_string, key=ord)
    result = sorted_string[:87]
    result.sort(reverse=True)
    return result
