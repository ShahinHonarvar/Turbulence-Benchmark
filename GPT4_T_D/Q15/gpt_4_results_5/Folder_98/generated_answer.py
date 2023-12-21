
def sum_odd_ints_inclusive(int_list):
    relevant_list = int_list[:7]
    odd_sum = sum([num for num in relevant_list if num % 2 != 0])
    return odd_sum
