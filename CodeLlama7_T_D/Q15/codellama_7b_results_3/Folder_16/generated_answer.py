
def sum_odd_ints_inclusive(my_list):
    start = 33
    end = 36
    odd_ints = []
    for i in range(start, end + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return sum(odd_ints)
