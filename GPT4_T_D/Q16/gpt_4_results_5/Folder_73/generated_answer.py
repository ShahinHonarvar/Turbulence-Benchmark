
def sum_even_ints_inclusive(input_list):
    sum = 0
    for i in range(19, 93):
        if i < len(input_list) and input_list[i] % 2 == 0:
            sum += input_list[i]
    return sum
