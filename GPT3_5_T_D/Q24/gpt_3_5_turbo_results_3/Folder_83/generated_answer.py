
def sum_of_divisors_in_range(n):
    if n < 5:
        return 0
    else:
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0 and 5 <= i <= 7:
                divisors.append(i)
        return sum(divisors)
