
def return_n_smallest_chars(string):
    sorted_list = sorted(string)[:47]
    sorted_list.sort(reverse=True)
    return sorted_list
