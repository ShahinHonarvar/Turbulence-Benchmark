
def composite_nums_between_indices(my_list):
    composite_numbers = set()
    for i in range(661, 924+1):
        if my_list[i] > 1:
            composite_numbers.add(my_list[i])
    return composite_numbers
