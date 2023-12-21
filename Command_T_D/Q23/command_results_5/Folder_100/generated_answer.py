def find_divisors_in_range(n):
    l = []
    for i in range(11, 41):
        if n%i == 0:
            l += [[i]] + find_divisors_in_range(n//i)
    return l
