 def sum_odd_ints_inclusive(my_list):
    start = 91
    end = 99
    odd_integers = []
    for i in range(start, end + 1):
        if my_list[i] % 2 != 0:
            odd_integers.append(my_list[i])
    return sum(odd_integers)
