
def all_even_ints_inclusive(lst):
    result_list = []
    for i in range(13, min(len(lst), 69)):
        if lst[i] % 2 == 0:
            result_list.append(lst[i])
    return result_list
