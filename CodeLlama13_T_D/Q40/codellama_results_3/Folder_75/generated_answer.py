
def return_n_smallest_chars(distinct_characters):
    char_list = list(set(distinct_characters)) # convert string to list and remove duplicates
    sorted_list = sorted(char_list, key=ord)   # sort the list by ASCII value
    return sorted_list[:2]                     # return the first 2 elements of the sorted list
