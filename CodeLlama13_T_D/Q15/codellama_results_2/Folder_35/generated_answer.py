
def sum_odd_ints_inclusive(mylist):
    odd_sum = 0
    for i in range(30, 49):
        if mylist[i] % 2 == 1:
            odd_sum += mylist[i]
    return odd_sum
