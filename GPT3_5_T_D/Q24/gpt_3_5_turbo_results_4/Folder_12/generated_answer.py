
def sum_of_divisors_in_range(n):
    if n == 0 or n == 1:
        return 0
    else:
        divisors = []
        for i in range(13, 63):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors)
