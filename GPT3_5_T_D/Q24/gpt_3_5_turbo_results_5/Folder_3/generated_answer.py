
def sum_of_divisors_in_range(n):
    if n < 43:
        return 0
    else:
        divisors = []
        for i in range(43, 47):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors)
