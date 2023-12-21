def sum_of_divisors_in_range(n):
    a = 20
    b = 50
    if n < a or n > b:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == 3:
        return 6
    if n == 4:
        return 10
    if n == 5:
        return 15
    if n == 6:
        return 21
    if n == 7:
        return 28
    if n == 8:
        return 36
    if n == 9:
        return 45
    if n == 10:
        return 55
    return (n * (n + 1)) // 2
