def sum_of_divisors_in_range(n):
    i = 46
    j = 65
    sum_ = 0
    while i <= j:
        if n % i == 0:
            sum_ += i
        elif n % j == 0:
            sum_ += j
        i += 1
        j -= 1
    return sum_
