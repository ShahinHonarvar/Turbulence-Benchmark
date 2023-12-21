
def sum_in_range(lst):
    sum = 0
    for num in lst:
        if -8 <= num <= 8:
            sum += num
    return sum
