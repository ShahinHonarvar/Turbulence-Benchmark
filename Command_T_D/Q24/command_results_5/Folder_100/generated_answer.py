def sum_of_divisors_in_range(n):
    for i in range(11, 41):
        if n%i == 0:
            n //= i
            break
    return n
