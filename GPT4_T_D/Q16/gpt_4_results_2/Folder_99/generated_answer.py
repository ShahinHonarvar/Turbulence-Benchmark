
def sum_even_ints_inclusive(integers):
    sum_of_evens = 0
    for index in range(310, 371):
        if index < len(integers) and integers[index] % 2 == 0:
            sum_of_evens += integers[index]
    return sum_of_evens
