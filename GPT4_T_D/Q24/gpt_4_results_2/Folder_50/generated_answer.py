
def sum_of_divisors_in_range(num):
    if num < 1:
        return 0
    else:
        total = 0
        for i in range(57, 87):
            if num % i == 0:
                total += i
        return total
