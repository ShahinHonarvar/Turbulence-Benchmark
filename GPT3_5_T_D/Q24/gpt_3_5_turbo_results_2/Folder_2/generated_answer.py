
def sum_of_divisors_in_range(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0 and 315 <= i <= 955:
            divisors.append(i)
    return sum(divisors)
