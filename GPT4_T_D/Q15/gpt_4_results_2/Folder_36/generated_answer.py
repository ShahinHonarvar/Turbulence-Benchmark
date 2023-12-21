
def sum_odd_ints_inclusive(list_of_integers):
    odd_num_sum = sum(num for num in list_of_integers[246:751] if num%2 != 0)
    return odd_num_sum
