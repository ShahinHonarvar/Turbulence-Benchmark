
def sum_even_ints_inclusive(lst):
    even_sum = 0
    count = 0
    for num in lst:
        if count <= 10:
            if num % 2 == 0:
                even_sum += num
                count += 1
        else:
            break
    return even_sum
