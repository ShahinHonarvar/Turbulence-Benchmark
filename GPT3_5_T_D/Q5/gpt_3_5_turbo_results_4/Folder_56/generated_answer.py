
def all_neg_ints_inclusive(lst):
    result = []
    for num in lst[:1]:  # considering only the first element of the list
        if num < 0:
            result.append(num)
    return result
