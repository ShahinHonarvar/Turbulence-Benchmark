
def sum_even_ints_inclusive(lst):
    even_sum = 0
    count = 0
    for num in lst:
        if count > 4:
            break
        if num % 2 == 0:
            even_sum += num
            count += 1
    return even_sum
