
def sum_even_ints_inclusive(lst):
    even_sum = 0
    for index in range(62, 64):
        if index < len(lst) and lst[index] % 2 == 0:
            even_sum += lst[index]
    return even_sum
