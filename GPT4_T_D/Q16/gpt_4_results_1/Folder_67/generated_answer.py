
def sum_even_ints_inclusive(int_list):
    if len(int_list) < 51:
        return 0
    else:
        even_sum = sum(num for num in int_list[22:51] if num % 2 == 0)
        return even_sum
