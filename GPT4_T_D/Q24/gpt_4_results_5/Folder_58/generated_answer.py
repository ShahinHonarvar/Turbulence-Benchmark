
def sum_of_divisors_in_range(num):
    summ = 0
    for i in range(403, 515):
        if num % i == 0:
            summ += i
    return summ
