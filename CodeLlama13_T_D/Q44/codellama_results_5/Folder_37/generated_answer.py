
def composite_nums_between_indices(list_of_positive_integers):
    composite_nums = set()
    for i in range(6):
        if list_of_positive_integers[i] > 1:
            composite_nums.add(list_of_positive_integers[i])
    return composite_nums
