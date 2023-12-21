
def return_n_smallest_chars(string):
    if len(string) < 27:
        return None
    sorted_list = sorted(string, key=ord)
    return sorted_list[:27][::-1]
