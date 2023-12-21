def sum_of_divisors_in_range(n):
    if n < 60 or n > 87:
        return 0
    divs = [i for i in range(1, n + 1) if n % i == 0]
    divs = [x for x in divs if 59 <= x <= 88]
    return sum(divs)
