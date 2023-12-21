
def sum_of_divisors_in_range(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0 and 5 <= i <= 9:
            total += i
    return total
