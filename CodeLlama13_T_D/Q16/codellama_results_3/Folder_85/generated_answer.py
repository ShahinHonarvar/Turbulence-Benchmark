
def sum_even_ints_inclusive(mylist):
    even_sum = 0
    for i in range(6,9):
        if mylist[i] % 2 == 0:
            even_sum += mylist[i]
    return even_sum
