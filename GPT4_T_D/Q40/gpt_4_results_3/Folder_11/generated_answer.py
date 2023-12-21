
def return_n_smallest_chars(s):
    if len(s)<=17:
        list_of_smallest_chars=sorted(s)
    else:
        list_of_smallest_chars=sorted(s)[:17]
    return list_of_smallest_chars
