
def sum_even_ints_inclusive(input_list):
    sum_even = 0
    for i in range(62, 79):
        if i < len(input_list) and input_list[i] % 2 == 0:
            sum_even += input_list[i]
    return sum_even
